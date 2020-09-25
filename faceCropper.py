import os
# from face_cropper import crop

# cropped_image = crop(
#     image_path= "/disk/projectEyes/faceCropper/anantOriginal.jpg",
#     saving_path= "/disk/projectEyes/faceCropper"
# )
import dlib 
import cv2
# JohnAbraham pic link: /disk/projectEyes/faceCropper/ja_256_8_10.jpg
ja = cv2.imread("/disk/projectEyes/faceCropper/anant_256_12_00.jpg")
# ben = cv2.imread("/disk/projectEyes/faceCropper/ben.jpg")
# benrgb = cv2.cvtColor(ben, cv2.COLOR_BGR2RGB)
jargb = cv2.cvtColor(ja,cv2.COLOR_BGR2RGB)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/disk/projectEyes/faceCropper/shape_predictor_68_face_landmarks.dat")

face_rect = detector(ja, 1)
shape = predictor(jargb, face_rect[0])
#Left eye:
p_36 = shape.part(36)
p_37 = shape.part(37)
p_38 = shape.part(38)
p_39 = shape.part(39)
p_40 = shape.part(40)
p_41 = shape.part(41)
mid_l_x = (p_36.x + p_39.x)//2 
mid_l1_y = (p_36.y + p_39.y)//2
mid_l2_y = (p_37.y + p_41.y)//2
mid_r_x = (shape.part(42).x + shape.part(45).x)//2
mid_r1_y = (shape.part(42).y + shape.part(45).y)//2
mid_r2_y = (shape.part(43).y + shape.part(47).y)//2 

for i in range(0,68):
    if i%10 == 0:
        print(str(shape.part(i).x) + " " + str(shape.part(i).y))
    else:
        print(str(shape.part(i).x) + " " + str(shape.part(i).y), end = ' ')
print("Done")
