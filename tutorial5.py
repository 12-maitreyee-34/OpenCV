#colours and colour detection
import cv2
import numpy as np

cam = cv2.VideoCapture(0)  #cv2.VideoCapture(0) is used to load the camera where 0 means the default webcam present at index 1
while True:
    ret,frame = cam.read()
    height= int(cam.get(4))  #gets the width and heght of the video capture or the frame inorder to draw a canvas
    width = int(cam.get(3))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color = np.array([35,40,40])
    upper_color = np.array([85,255,255])
    mask = cv2.inRange(hsv, lower_color,upper_color)
    result= cv2.bitwise_and(frame,frame ,mask=mask)
    

    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",result)
    if cv2.waitKey(1)== ord('e'):
        break
cam.release()
cv2.destroyAllWindows
