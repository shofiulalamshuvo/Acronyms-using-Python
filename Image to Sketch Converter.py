#importing open cv
import cv2
image = cv2.imread("captain america.jpg")  #add the image which you want to convert 
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_img)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_img, invertedblur, scale= 256.0)

cv2.imwrite("sketch.png", sketch) #get the sketch file or outpu as png file
