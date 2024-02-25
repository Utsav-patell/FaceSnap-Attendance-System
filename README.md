# FaceTrack-Attendance-System
Its an Facial Base attendance System in which the attendance will be marked automatically (for testing purpose I have kept a condition that if 'p' is pressed then only attendance will be marked) and it is stored in the database (for Hackathon I have used SQL)

## 1) Add_Student.py 
This file will help to add the student to the database by capturing the face of the student using webcam.
## 2) Model.py 
It is the main face recgonization model which will recognize whose face is in the webcam and match it with the database images and give the id of image related to it.
## 3) Take_Attendance.py 
This file will capture real time faces and will match it with the datbase images and then Provide related id of the image.

_Pre-model is the algorithm which will realtime detect the nodes of the faces._

## 4) Remove_Students.py
This will help to remove the student from the database just not only the images but also the encodings of the images from the model so that it does not get predicted.

## 5) Show_details.py
This will provide all the previous attendance of the students marked inshort it is a database of the attendance list. Currently i have stored the attendance list in cvs files and in near future I will use the sql database.

## 6) main.py
Use this to use this project it contains all the operations of the project.


