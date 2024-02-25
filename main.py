import take_attendence
import remove_student
import model
import add_student
import student_details
# import backend


while True:
    print("1. Press [1] to add student")
    print("2. Press [2] to take attendance")
    print("3. Press [3] to remove student")
    print("4. Press [4] to get student details")
    print("5. Press [5] to exit ")
    print("***********************************")
    i = input("Enter Your Choice: ")
    if i == '5':
        print("Good Bye\n")
        break
    elif i == '1':
        add_student.create_student()
        add_student.take_image()
        model.get_data()
        model.get_encoding()
        model.create_encode_file()
    elif i == '2':
        take_attendence.load_encoded_file()
        take_attendence.load_student_info()
        take_attendence.today_date()
        take_attendence.take_image()
    elif i == '3':
        remove_student.delete_student()
        model.get_data()
        model.get_encoding()
        model.create_encode_file()     
    elif i == '4':
        student_details.read_csv()
        student_details.combine_dataframe()
        student_details.get_student_details()     
    else:
        print("Enter valid Input\n")