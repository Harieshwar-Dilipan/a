import cv2

image=cv2.imread('solar-system.jpg')
cv2.putText(image,'sun',(70,50),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
cv2.putText(image,'mercury',(100,250),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),2)
cv2.putText(image,'venus',(170,180),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),2)
cv2.putText(image,'earth',(250,270),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
cv2.putText(image,'mars',(350,180),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
cv2.putText(image,'jupiter',(550,50),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
cv2.putText(image,'saturn',(700,120),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
cv2.putText(image,'uranus',(900,120),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)
cv2.putText(image,'neptune',(1100,120),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,255,255),2)

cv2.imshow('img',image)

cv2.waitKey(3000)