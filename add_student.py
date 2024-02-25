import cv2 
import os
import json
# print(cv2.__version__)



class student():
    def __init__(self):
        self.name = input("Enter the name of the student: ")
        self.en_no = input("Enter Your Enrollment Number: ")
        self.branch = input("Enter the branch of the Student: ")
        self.create_dict()
        
    def create_dict(self):
        self.student_info = {
            self.en_no:{"name":self.name,
                        "branch":self.branch,  
            }
        }
    def new_student(self):
        if "student_info.json" in os.listdir("./FaceSnap-Attendance-System/database"):
            with open("./FaceSnap-Attendance-System/database/student_info.json","r",encoding="utf-8") as file:
                temp_dict = json.load(fp=file)
            temp_dict.update(self.student_info)
            with open("./FaceSnap-Attendance-System/database/student_info.json","w",encoding="utf-8") as file:
                json.dump(temp_dict,fp=file)
        else:
            with open("./FaceSnap-Attendance-System/database/student_info.json","w") as file:
                json.dump(self.student_info,fp=file)
        

def create_student():
    global s1 
    s1 = student()

def take_image():
    cam = cv2.VideoCapture(0)
    image_no=0
    while True:
        is_capturing,frame = cam.read()
        frame = cv2.flip(frame,1)
        k = cv2.waitKey(1)
        cv2.putText(frame,str(image_no),org=(50,50),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0),thickness=1,)
        if is_capturing:
            cv2.imshow("web cam",frame)
            # image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            
            if k == ord('c'):

                cv2.imwrite(filename=f"./FaceSnap-Attendance-System/database/assets/{s1.en_no}.jpg",img = frame)
                image_no+=1
        if image_no==1 or k == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    s1.new_student()

if __name__ == "__main__":
    create_student()
    take_image()
    
