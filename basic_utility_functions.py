import cv2
import os
img=cv2.imread(r"C:\Users\User\OneDrive\open cv\open cv images\OIP.webp")
#cv2.imshow("bg image",img)
print(img)
resized_img=cv2.resize(img,(1500,1200))
#cv2.imshow("resized image",resized_img)
img2=cv2.imread(r"C:\Users\User\OneDrive\open cv\open cv images\clouds-cloudy-conifers-247478.jpg")
#cv2.imshow("bg image",img2)

resized_img2=cv2.resize(img2,(1500,1200))
#cv2.imshow("resized image",resized_img2)
combination_img=cv2.addWeighted(resized_img,0.9,resized_img2,0.9,0)
cv2.imshow("combination",combination_img)
cv2.waitKey(0)