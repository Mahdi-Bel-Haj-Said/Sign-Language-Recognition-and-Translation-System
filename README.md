# Sign-Language-Recognition-and-Translation-System
This project is an AI-powered sign language recognition and translation system built using Python, TensorFlow, OpenCV, Scikit-learn, and MediaPipe. The system detects hand gestures in real time and translates them into text, providing an inclusive communication tool for the deaf and hard-of-hearing community.

The application can be integrated into communication and meeting platforms (e.g., Zoom, Teams, Google Meet) to enhance accessibility and make digital conversations more inclusive.

## 🚀 Features
- Real-time **hand gesture recognition**   
- Gesture-to-**text translation** 
- Extensible for multiple sign languages   
- Integration potential with communication platforms   
## 🛠️ Tech Stack
- **Python**  
- **TensorFlow**  
- **OpenCV**  
- **Scikit-learn**  
- **MediaPipe**

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/Mahdi-Bel-Haj-Said/Sign-Language-Recognition-and-Translation-System.git
cd Sign-Language-Recognition-and-Translation-System
pip install -r requirements.txt
```

## Train the model (optional if you use pre-trained model) 
1) open collect_imgs.py 
alter the line 34 and chose how many classes you want to add to the model by changing the number of classes to capture in the code 
```bash
    parser.add_argument('--classes', type=int, default=3, help='Number of classes to capture')
```
3) run collect_imgs.py 
python src/train.py 

## Run real-time recognition
python src/recognize.py
