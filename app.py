# IMPORTS
from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
import mediapipe as mp
import pandas as pd
import numpy as np
import base64
import pickle
import cv2
import os

# INITIALIZATION
app = Flask(__name__)
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True,
                    model_complexity=2,
                    enable_segmentation=True,
                    min_detection_confidence=0.5)

# LOADING MODEL
with open('detect_pose.pkl', 'rb') as f:
    model = pickle.load(f)

# YOGA POSE DETECTION USING IMAGE
def usingImage(img_path):
    input_frame = cv2.imread(img_path)
    result = pose.process(image=input_frame)
    output_image = input_frame.copy()
    label = "Unknown Pose"
    accuracy = 0
    try:
        mp_drawing.draw_landmarks(image=output_image, landmark_list=result.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS)
        pose_landmarks = result.pose_landmarks.landmark
        row = list(np.array([[landmark.x, landmark.y, landmark.z]
                             for landmark in pose_landmarks]).flatten())
        X = pd.DataFrame([row])
        label = model.predict(X)[0]
        body_language_prob = model.predict_proba(X)[0]
        accuracy = str(
            round(body_language_prob[np.argmax(body_language_prob)]*100, 3))
        if(float(accuracy) < 50):
            label = "Unknown Pose"
        cv2.rectangle(output_image, (0, 0), (250, 60),
                      (0, 0, 255), 1, cv2.LINE_4)
        cv2.putText(output_image, 'Class', (5, 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_4)
        cv2.putText(output_image, label, (5, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_4)
        cv2.putText(output_image, 'Accuracy', (150, 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_4)
        cv2.putText(output_image, accuracy, (150, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_4)
        retval, buffer = cv2.imencode('.jpg', output_image)
        jpg_as_text = base64.b64encode(buffer)
        return(jpg_as_text)
    except:
        return('')

# YOGA POSE DETECTION USING WEBCAM
def usingWebcam():
    camera = cv2.VideoCapture(0)
    while(True):
        status, input_frame = camera.read()
        if(status == False):
            break
        else:
            result = pose.process(image=input_frame)
            label = "Unknown Pose"
            accuracy = 0
            try:
                mp_drawing.draw_landmarks(image=input_frame, landmark_list=result.pose_landmarks,
                                          connections=mp_pose.POSE_CONNECTIONS)
                pose_landmarks = result.pose_landmarks.landmark
                row = list(np.array([[landmark.x, landmark.y, landmark.z]
                                     for landmark in pose_landmarks]).flatten())
                X = pd.DataFrame([row])
                label = model.predict(X)[0]
                body_language_prob = model.predict_proba(X)[0]
                accuracy = str(
                    round(body_language_prob[np.argmax(body_language_prob)]*100, 3))
                if(float(accuracy) < 50):
                    label = "Unknown Pose"
            except:
                pass
            cv2.rectangle(input_frame, (0, 0), (250, 60),
                          (0, 0, 255), 1, cv2.LINE_4)
            cv2.putText(input_frame, 'Class', (5, 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_4)
            cv2.putText(input_frame, label, (5, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_4)
            cv2.putText(input_frame, 'Accuracy', (150, 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_4)
            cv2.putText(input_frame, str(accuracy), (150, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_4)
        ret, buffer = cv2.imencode('.jpg', input_frame)
        input_frame = buffer.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + input_frame + b'\r\n')

# ENDPOINTS
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/webcam')
def webcam():
    return(render_template('webcam.html'))


@app.route('/video_capture')
def video_capture():
    return(Response(usingWebcam(), mimetype='multipart/x-mixed-replace; boundary=frame'))


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'upload', secure_filename(f.filename))
        f.save(file_path)
        predictions = usingImage(file_path)
        return predictions
    return None


# MAIN
if __name__ == "__main__":
    app.run(debug=True)
