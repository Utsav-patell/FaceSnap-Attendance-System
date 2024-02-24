import cv2 
import pickle
import json
import face_recognition
import numpy as np
import cvzone
import os
import csv
from datetime import datetime
from pygame import mixer
# print(cv2.__version__)
def play_music(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
     
def save_csv(info_dict):
    if f"{cur_date}.csv" in os.listdir("./FaceTrack-Attendance-System/csv_files"):
        with open(f"./FaceTrack-Attendance-System/csv_files/{cur_date}.csv","a") as csv_file:
            titles = ["Enrollment No","Name","Branch","Date","Day","Time"]
            writer = csv.DictWriter(csv_file,titles)
            writer.writerow(info_dict)
    else:
        with open (f"./FaceTrack-Attendance-System/csv_files/{cur_date}.csv","w") as csv_file:
            titles = ["Enrollment No","Name","Branch","Date","Day","Time"]
            writer = csv.DictWriter(csv_file,titles)
            writer.writeheader()
            writer.writerow(info_dict)
            
            
            

def load_encoded_file():
    global old_encoded_image,en_no_list
    with open('./FaceTrack-Attendance-System/database/enc_img_eno_list.p','rb') as file: 
        old_encoded_image,en_no_list = pickle.load(file=file)


def load_student_info():
    global student_dict
    with open('./FaceTrack-Attendance-System/database/student_info.json','r') as file: 
        student_dict = json.load(fp=file)
        
def today_date():
    global cur_day,cur_time,cur_date
    cur_date = datetime.now().date()
    cur_time = datetime.now().ctime().split(" ")[3]  #'Mon', 'Feb', '12', '19:11:11', '2024'
    cur_day =  datetime.now().ctime().split(" ")[0]

# print(en_no_list)

def take_attendasnce(k,resize_image):
    if k == ord('p'):
        roi_location = face_recognition.face_locations(resize_image)
        new_encoded_images = face_recognition.face_encodings(resize_image,roi_location)

        for encoded_face,face_loc in zip(new_encoded_images,roi_location):
            matches = face_recognition.compare_faces(old_encoded_image,encoded_face)
            face_distance = face_recognition.face_distance(old_encoded_image,encoded_face) # Confidence
            # print(f"matches = {matches}")
            # print(f"distance = {face_distance}")
            predicted_index = np.argmin(face_distance)
            if matches[predicted_index] and face_distance[predicted_index]<0.5:
                play_music("./FaceTrack-Attendance-System/database/Correct_ans.mp3")
                match_key = en_no_list[predicted_index]
                info_dict = {
                    "Name":student_dict[match_key]['name'],
                    "Enrollment No": match_key,
                    "Branch": student_dict[match_key]['branch'],
                    "Date":cur_date,
                    "Day":cur_day,
                    "Time":cur_time
                }
                print(matches)
                print(face_distance)
                print(face_distance[predicted_index])
                print(student_dict[match_key]['name'])
                save_csv(info_dict)
                
                # print(f"face_distance = {face_distance[predicted_index]}")
                # print(f"En rollment number = {en_no_list[predicted_index]}")
            else:

                print("Unknown")


def take_image():
    face_capture = "./FaceTrack-Attendance-System/pre-model/haarcascade_frontalface_default.xml"
    cam = cv2.VideoCapture(0)
    face_box = cv2.CascadeClassifier(face_capture)

    while True:
        is_capturing,frame = cam.read()
        frame = cv2.flip(frame,1)
        face_coordinates = face_box.detectMultiScale(frame,minSize=(30,30),minNeighbors=5,scaleFactor=1.3)
        k = cv2.waitKey(1)
        
        if is_capturing:
            if len(face_coordinates):
                for(x,y,w,h) in face_coordinates:
                    cvzone.cornerRect(frame,(x,y,w,h),rt=0)
                    resize_image = cv2.resize(frame,(0,0),None,0.25,0.25)
                    resize_image = cv2.cvtColor(resize_image,cv2.COLOR_BGR2RGB) 
                    take_attendasnce(k,resize_image)
                
            else:
                if k == ord('p'):
                    print("No face detected")
            cv2.imshow("web cam",frame)
        if k == ord('q'):
            break    


    cam.release()
    cv2.destroyAllWindows()       
    # image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            
def capture():
    load_encoded_file()
    load_student_info()
    today_date()
    take_image()
if __name__=="__main__":
    capture()

