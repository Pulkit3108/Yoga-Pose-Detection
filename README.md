# Yoga Pose Detection
A Web App that is made using Flask Web Framework in Python to Detect Yoga Pose with the help of landmarks that are located using Mediapipe Library. The user can either upload image or can use a webcam. Currently, It can detect 5 poses (Downdog, Goddess, Plank, Tree, Warrior II). The Model is trained by storing the landmarks on the images in a CSV file which is then passed to 5 different Machine Learning Classifiers (Logistic Regression, Ridge Classifier, Random Forest Classifier, K-Nearest Neighbors Classifier, Gradient Boosting Classifier), and the one with the highest accuracy is selected. 
*The accuracy is approximately **96%***

Link to Dataset: https://www.kaggle.com/niharika41298/yoga-poses-dataset
## Working

![Picture1](https://github.com/user-attachments/assets/c16be833-8a17-4457-824f-5843ed832da9)

![Picture1](https://github.com/user-attachments/assets/28a02cdf-ad3e-4aec-be3e-b809a9b3aef9)

