import cv2
#load an image
bridge_img = cv2.imread("assests/bridge.jpeg", 1)
tree_img = cv2.imread("assests/tree.jpeg", -1)

#Resize the image
bridge_img = cv2.resize(bridge_img, (224,224))
tree_img = cv2.resize(tree_img,(0,0),fx=2,fy=2)

#Rotate image
bridge_img = cv2.rotate(bridge_img, cv2.ROTATE_90_COUNTERCLOCKWISE)

#Display image
cv2.imshow('Bridge',bridge_img)
cv2.imshow('Tree',tree_img)

#Close the window
cv2.waitKey(0)
cv2.destroyAllWindows()