#  Sign Language Recognition and Translation System
## Overview 
This project is an AI-powered sign language recognition and translation system built using Python, TensorFlow, OpenCV, Scikit-learn, and MediaPipe.
The system detects hand gestures in real time and translates them into text, providing an inclusive communication tool for the deaf and hard-of-hearing community.

The application can be integrated into communication and meeting platforms (e.g., Zoom, Teams, Google Meet) to enhance accessibility and make digital conversations more inclusive.
## 🚀 Features
- Real-time **hand gesture recognition**   
- Gesture-to-**text translation** ✍️ 
- Extensible for multiple sign languages 
- Integration potential with communication platforms   

---

## 🛠️ Tech Stack
- **Python**  
- **TensorFlow**  
- **OpenCV**  
- **Scikit-learn**  
- **MediaPipe**

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/Mahdi-Bel-Haj-Said/Sign-Language-Recognition-and-Translation-System.git
cd Sign-Language-Recognition-and-Translation-System
# Create python virtual envirement for the project (venv)
# Install dependencies
pip install -r requirements.txt
```

## Usage 
1) Run Collect_imgs.py to add the gestures and also you can change thee number of cloasses to capture that specifies the number of signs you gonna add to the your model
```bash
    parser.add_argument('--classes', type=int, default=3, help='Number of classes to capture')
```
2) add that the text/transition for the signs by order 
```bash
    labels_dict = {0: 'A', 1: 'B', 2: 'L'}
```
3) collect data by running collect_imgs.py and doing the signs or the gestures and try to move your hand in different directions (up, down, left, right, zoom in, zoom out) to grantie the best accuracy
4) Create the dataset by running Create_dataset.py 
5) Run the app 

## The application 
<img width="798" height="622" alt="Capture d'écran 2025-08-21 131144" src="https://github.com/user-attachments/assets/b23154e6-7c9f-4519-9bb4-ad0806a4441c" />
<img width="791" height="632" alt="image" src="https://github.com/user-attachments/assets/438477c1-5ff4-41b3-b0c4-23901661ed1f" />
<img width="797" height="632" alt="fdsgdfgdfg" src="https://github.com/user-attachments/assets/a3b4e5b2-a3f1-402f-bd1a-05717a4a02cf" />




 
