import cv2
import face_recognition
import pickle
import os

def get_data():
    global image_list,en_no_list
    image_list = []
    en_no_list = []
    
    
    data_path = './database/assets'
    images_path = os.listdir(path=data_path)
    # print(images_name)
    for image_path in images_path:
        # print(os.path.join(data_path,image_path))
        image_list.append(cv2.imread(os.path.join(data_path,image_path)))
        en_no_list.append(os.path.splitext(image_path)[0])
        
    print(len(image_list))
    print(len(en_no_list))

def get_encoding():
    global encoded_image_list
    encoded_image_list = []
    for image in image_list:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        encoded_image = face_recognition.face_encodings(image)[0]
        encoded_image_list.append(encoded_image)
        
    print(type(encoded_image))
    print(len(encoded_image))


# print(encoded_img_eno_list)


def create_encode_file():
    encoded_img_eno_list = []
    encoded_img_eno_list = [encoded_image_list,en_no_list]
    with open('./database/enc_img_eno_list.p','wb') as file:
        pickle.dump(encoded_img_eno_list,file=file)
    print('file saved')


 
if __name__ == "__main__":
    get_data()
    get_encoding()
    create_encode_file()