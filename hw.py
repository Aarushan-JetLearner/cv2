import cv2
import os
img1=r"C:\Users\User\OneDrive\open cv\open cv images\landscape.jpg"
img=cv2.imread(r"C:\Users\User\OneDrive\open cv\open cv images\landscape.jpg")
cv2.imshow("landscape jpg",img)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("landscape jpg2",img2)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("landscape jpg3",img3)

img4=r"C:\Users\User\OneDrive\open cv\open cv images"
os.chdir(img4)
cv2.imwrite("greyscale2.png",img2)
cv2.imwrite("HSV.png",img3)
cv2.waitKey(0)