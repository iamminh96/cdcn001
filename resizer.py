import cv2

img = cv2.imread("temp.png")
img = cv2.resize(img , (1600 , 900) , interpolation = cv2.INTER_CUBIC)

cv2.imwrite("restful.png" , img)