# Yoga Pose Detection
A Web App which is made using Flask Web Framework in Python to detect Yoga Pose with the help of landmarks that are plotted using Mediapipe Library. The user can either upload image or can use webcam.
Currently, It can detect 5 poses (Downdog, Goddess, Plank, Tree, Warrior II).
The Model is trained by storing the landmarks on the images in a csv file which is then passed to 5 different maching learning algorithms (Logistic Regression, Ridge Classifier, Random Forest Classifier, Gradient Boosting Classifier, K-Neighbors Classifier) and the one with highest accuracy is selected. 
The acccuracy is approximately 97%

Link to Dataset: https://www.kaggle.com/niharika41298/yoga-poses-dataset
## Working
> Using Image

![](https://i.imgur.com/PDsg3oT.gif)
> Using Video

![](https://i.imgur.com/5EFYw15.gif)
> No Landmarks

![](https://i.imgur.com/dUnnIR8.gif)
