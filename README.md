# Gaze-correction-imagePreprocessing
Face cropper doc \
Git link: https://github.com/anantthebiker/Gaze-correction-imagePreprocessing \
Goal: How to get a perfect cropped image for Gaze-correction? \
Gaze Correction link: https://github.com/anantthebiker/EyeContactCorrection_with_FrozenModel 
1)	Set image’s(Original image) path in facecropper.py 
2)	If there is a single face, it will print its 68 point landmark on the terminal. Copy that.
3)	For further cropping based on the landmark pts, paste all 68 landmarks in: faceCropper/HD-CelebA-Cropper/data/landmark.txt after the name of the image. Like this(excluding ""):
    "ben.jpg 68 161 69 183 72 …….." 
4)	Add the original image in: faceCropper/HD-CelebA-Cropper/data/img_celeba
5)	Now run “align.py” after modifying a few hardcoded directories. 
6)	The cropped output should get saved in: faceCropper/HD-CelebA-Cropper/data/aligned 
7)	(OPTIONAL to get new coordinates on the Cropped image) Now you can use the just cropped image as a new original image to facecropper.py  and put breakpoints @ line 33, to see center coordinates of Left and right eyes or print any other coordinate that you wish.
