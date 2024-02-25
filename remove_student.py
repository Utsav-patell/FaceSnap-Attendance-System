import os
import pickle


def load_encoded_file():
    global en_no
    en_no = input("Enter the en_no to remove: ")
    global encoded_img
    global en_no_list
    with open('./FaceTrack-Attendance-System/database/enc_img_eno_list.p','rb') as file: 
        encoded_img,en_no_list = pickle.load(file=file)

def remove_enno(en_no_list):
    global target_index
    if en_no in en_no_list:
        target_index = en_no_list.index(en_no)
        en_no_list.pop(target_index)
        print(f"{en_no} removed Succesfully")
    else:
        print("Number not present")

def remove_encoded_image(encoded_image_list):
        encoded_image_list.pop(target_index)
        print("Image encodings removed")


def remove_image(en):
    path = "./FaceTrack-Attendance-System/database/assets"
    images = os.listdir(path=path)
    # print(images)
    # print(os.path.splitext(images[0]))
    for image in images:
        if en in os.path.splitext(image):
            image_path = os.path.join(path,image)
            os.remove(image_path)
            print("Image removed")
            
def create_encode_file():
    encoded_img_eno_list = [encoded_img,en_no_list]
    with open('./FaceTrack-Attendance-System/database/enc_img_eno_list.p','wb') as file:
        pickle.dump(encoded_img_eno_list,file=file)
    print('file saved')

def delete_student():
    load_encoded_file()
#     Remove en_no from list
    if en_no in en_no_list:
        remove_enno(en_no_list) # Enno list
#     Remove Image from data base
        remove_encoded_image(encoded_img) # encoded image list
#     Remove_image(en_no)
        remove_image(en_no)
#     Updating the list
        create_encode_file()
    else:
        print("Student not found. Plesae add the student first")
if __name__=="__main__":           
    delete_student()
    # print(encoded_img)
    # print(en_no_list)
    
        