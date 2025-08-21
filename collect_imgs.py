import os
import argparse

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


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
    parser.add_argument('--classes', type=int, default=3, help='Number of classes to capture')
    parser.add_argument('--size', type=int, default=100, help='Images per class to capture')
    args = parser.parse_args()

    number_of_classes = args.classes
    dataset_size = args.size

    cap = open_camera(args.camera)

    for j in range(number_of_classes):
        class_dir = os.path.join(DATA_DIR, str(j))
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

        print('Collecting data for class {}'.format(j))

        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                continue
            cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                        cv2.LINE_AA)
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) == ord('q'):
                break

        counter = 0
        while counter < dataset_size:
            ret, frame = cap.read()
            if not ret or frame is None:
                continue
            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)

            counter += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
