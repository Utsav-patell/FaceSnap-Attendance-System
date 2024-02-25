import pandas as pd
import os

def read_csv():
    global student_details
    student_details = []
    for files in os.listdir("./FaceSnap-Attendance-System/csv_files"):
        df = pd.read_csv(f"./FaceSnap-Attendance-System/csv_files/{files}")
        student_details.append(df)
# print(len(student_details))
def combine_dataframe():
    global combined_frame
    combined_frame = pd.concat(student_details)
    combined_frame = combined_frame.drop_duplicates(keep='last',subset=["Enrollment No","Date"],ignore_index=True)
    # print(combined_frame)




def get_student_details():
    print("The list of student Registerd are\n")
    print(combined_frame["Enrollment No"].unique())
    student_id = input("Enter the student id you want to see details ")
    if combined_frame[combined_frame["Enrollment No"]==student_id].empty:
        print("Student has either 0 present or not registered")   
    else:
        student_info = combined_frame[combined_frame["Enrollment No"]==student_id]
        
        print(student_info.to_string())
        # print(f"\n{student_info.to_string()}\n")
        print(f"\nTotal present of the student is {len(student_info)}\n")

if __name__=="__main__":
    read_csv()
    combine_dataframe()
    get_student_details()  
