#Accessing the webcam
import cv2
import numpy as np

cam = cv2.VideoCapture(0)  #cv2.VideoCapture(0) is used to load the camera where 0 means the default webcam present at index 1
while True:
    
    ret,frame = cam.read()
    height= int(cam.get(4))  #gets the width and heght of the video capture or the frame inorder to draw a canvas
    width = int(cam.get(3))  # 3 and 4 are the default values for width and height respectively .

    img = np.zeros(frame.shape, np.uint8)
    smaller_img = cv2.resize(frame,(0,0),fx=0.5 ,fy=0.5)
    img[:height//2,:width//2]= smaller_img
    img[height//2:,:width//2]= cv2.rotate(smaller_img,cv2.ROTATE_180)
    img[:height//2,width//2:]= smaller_img
    img[height//2:,width//2:]= cv2.rotate(smaller_img,cv2.ROTATE_180)

    cv2.imshow("Frame",img)
    if cv2.waitKey(1)== ord('e'):
        break
cam.release()
cv2.destroyAllWindows
