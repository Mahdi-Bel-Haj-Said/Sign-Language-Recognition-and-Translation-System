import pickle
import argparse
from collections import deque

import cv2
import mediapipe as mp
import numpy as np


def open_camera(preferred_index: int) -> cv2.VideoCapture:
    cap = cv2.VideoCapture(preferred_index)
    if cap.isOpened():
        print(f'Camera opened at index {preferred_index}')
        return cap

    print(f'Preferred camera index {preferred_index} failed. Trying other indices...')
    for idx in [0, 1, 2, 3]:
        if idx == preferred_index:
            continue
        cap_try = cv2.VideoCapture(idx)
        if cap_try.isOpened():
            print(f'Camera opened at fallback index {idx}')
            return cap_try
        cap_try.release()

    raise RuntimeError('Could not open any camera. Please check your webcam and indices.')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--camera', type=int, default=0, help='Camera index (default: 0)')
    parser.add_argument('--stable', type=int, default=5, help='Consecutive frames needed to accept a letter')
    parser.add_argument('--no-hand-frames', type=int, default=15, help='Frames with no hand before inserting space')
    parser.add_argument('--max-seq-len', type=int, default=32, help='Max characters to keep in sequence overlay')
    args = parser.parse_args()

    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']

    cap = open_camera(args.camera)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    labels_dict = {0: 'A', 1: 'B', 2: 'L'}

    # Debounce and translation state
    last_preds: deque[str] = deque(maxlen=max(3, args.stable))
    accepted_sequence: list[str] = []
    frames_without_hand = 0

    while True:

        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        current_char = None
        current_conf = 0.0

        if results.multi_hand_landmarks:
            frames_without_hand = 0
            # Use only the first detected hand to match training feature size
            hand_landmarks = results.multi_hand_landmarks[0]

            # Draw landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            # Predict and confidence
            probs = None
            try:
                probs = model.predict_proba([np.asarray(data_aux)])[0]
                pred_idx = int(np.argmax(probs))
                current_conf = float(probs[pred_idx])
            except Exception:
                pred_idx = int(model.predict([np.asarray(data_aux)])[0])
                current_conf = 1.0

            current_char = labels_dict[pred_idx]

            # Draw bounding box and prediction with confidence
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
            cv2.putText(
                frame,
                f"{current_char} ({int(current_conf*100)}%)",
                (x1, max(30, y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 0, 0),
                2,
                cv2.LINE_AA,
            )

            # Debounce logic
            last_preds.append(current_char)
            if len(last_preds) == last_preds.maxlen and len(set(last_preds)) == 1:
                if not accepted_sequence or accepted_sequence[-1] != current_char:
                    accepted_sequence.append(current_char)
                last_preds.clear()
        else:
            frames_without_hand += 1
            if frames_without_hand >= args.no_hand_frames:
                if accepted_sequence and accepted_sequence[-1] != ' ':
                    accepted_sequence.append(' ')
                frames_without_hand = 0
                last_preds.clear()

        # Render translation overlay
        seq_text = ''.join(accepted_sequence)[-args.max_seq_len:]
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (W, 50), (255, 255, 255), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        cv2.putText(frame, f"Seq: {seq_text}", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        if key == ord('c'):
            accepted_sequence.clear()
            last_preds.clear()
        if key == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
