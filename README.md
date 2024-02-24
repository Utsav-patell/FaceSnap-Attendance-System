# FaceTrack-Attendance-System
Its an Facial Base attendance System in which the attendance will be marked automatically (for testing purpose I have kept a condition that if 'p' is pressed then only attendance will be marked) and it is stored in the database (for Hackathon I have used SQL)

## 1) Add_Student.py 
This file will help to add the student to the database by capturing the face of the student using webcam.
## 2) Model.py 
It is the main face recgonization model which will recognize whose face is in the webcam and match it with the database images and give the id of image related to it.
## 3) Take_Attendance.py 
This file will capture real time faces and will match it with the datbase images and then Provide related id of the image.

_ pre-model is the algorithm which will realtime detect the nodes of the faces._


