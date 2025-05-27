#Drawing lines ,rectangle , circle and text
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    height = cap.get(4)
    img = cv2.line(frame, (0,0),(255,255), (100,10,70),5)
    img= cv2.rectangle(frame, (67,78),(100,100),(255,0,0),-1) #-1 fills the rectangle with color
    img = cv2.circle(frame, (255,255),60,(1,2,80),-1)
    font = cv2.FONT_HERSHEY_TRIPLEX
    img = cv2.putText(frame,"damnn!!", (200,200),font,2.0,(50,50,0),2,cv2.LINE_AA)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) == ord('e'):
        break
cap.release()
cv2.destroyAllWindows()

