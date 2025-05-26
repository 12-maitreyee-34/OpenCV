#Accessing the pixels: It is carried out through indexing and slicing 

import cv2
import random
img= cv2.imread("assests/bridge.jpeg", 1)
print(img.shape)
print(img[4][2])
print(img[5][2:6])

#Changing pixel colours

for i in range(120):
    for j in range(120):  # assuming you want a 120x120 patch
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


#Copy pasting a pat of image 
image=cv2.imread('assests/tree.jpeg',1)
cp= image[100:150, 120:140]  #slicing in numpy array..1st part is slicing of rows, 2nd part is slicing of columns
image[0:50, 20:40]    #this is how copy pasting is done
cv2.imshow("Changed pixel color",img)


cv2.imshow("Copy paste image",image)
cv2.waitKey(0)
cv2.destroyAllWindows