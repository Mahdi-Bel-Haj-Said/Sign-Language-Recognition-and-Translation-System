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
2) Add the text/transition for the signs as dictionary in order by modifying the file interference_classifier.py line 49 
```bash
    labels_dict = {0: 'A', 1: 'B', 2: 'L'}
```
3) run collect_imgs.py
```bash
python path/collect_imgs.py 
```
4) add the Signs that you want by pressing Q while moving you hand in different directions for 3 seconds for each class to garentie better accuracy (zoom in and zoom out right left up down)
5) once done run Create_dataset.py 
```bash
python path/Create_dataset.py 
```
## Run the application 
test and verify accuracy if something is wrong you can redo the images collect part 

# The application results 

<img width="791" height="632" alt="image" src="https://github.com/user-attachments/assets/be43c508-987b-44ca-b777-b6239971c737" />

<img width="797" height="632" alt="fdsgdfgdfg" src="https://github.com/user-attachments/assets/1f416dc5-80fc-4b69-9681-3916dc103e78" />

<img width="798" height="622" alt="Capture d'écran 2025-08-21 131144" src="https://github.com/user-attachments/assets/09e94ade-6c20-4fa1-975c-bb423691935b" />

