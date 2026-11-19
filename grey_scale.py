import cv2
import os
img=cv2.imread(r"C:\Users\User\OneDrive\open cv\open cv images\clouds-cloudy-conifers-247478.jpg")
cv2.imshow("background image",img)
#img2=cv2.imread(r"C:\Users\User\OneDrive\open cv\open cv images\clouds-cloudy-conifers-247478.jpg",0)
#cv2.imshow("background image",img2)

img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("background image",img3)
img4=r"C:\Users\User\OneDrive\open cv\open cv images"
os.chdir(img4)
cv2.imwrite("grey_scale.png",img3)
blue,green,red=cv2.split(img)
cv2.imshow("blue",blue)
cv2.imshow("red",red)
cv2.imshow("green",green)
cv2.waitKey(0)