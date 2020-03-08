import numpy as np
import cv2
#import imutils

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
image = cv2.imread('ERODE4.png',0)
#---- removing the noise 
#Gimg  = cv2.GaussianBlur(image,(7,7),0)
#image = cv2.erode(image,None,iterations=1)
image = cv2.dilate(image,None,iterations=1)

#cv2.imshow("erode",image)
#cv2.waitKey(0)
image = image[30:,:]
vehicle_count=0

image = cv2.dilate(image,None,iterations=5)
cv2.imwrite("dilated.png",image)
cv2.waitKey(0)

cnts, hierarchy = cv2.findContours(image, cv2.RNG_UNIFORM, cv2.CHAIN_APPROX_NONE)
multiple_contours = []
for c in cnts:
    orig = image.copy()
    area = cv2.contourArea(c)
    if area <1000:
        pass
    vehicle_count+=1
    print(area)
    box = cv2.minAreaRect(c)
    #print(box)
    #print(box)
    #cv2.imshow('counts',ximg)
    #cv2.waitKey(0)
    #cv2.drawContours(orig,c,-1,(139,131,255),3)
    #cv2.imshow("erotion",orig)
    multiple_contours.append(c)
    cv2.waitKey(0)
#ximg = cv2.dilate(orig,None,iterations=2)
#cv2.imshow("DILATION",ximg)
cv2.waitKey(0)
cv2.drawContours(orig,multiple_contours,-1,(139,131,255),2)
#cv2.putText(orig,str(vehicle_count),(10,90),cv2.FONT_HERSHEY_COMPLEX,1,(139,131,255),2)
cv2.imshow("IMAGE",orig)
cv2.waitKey(0)
#cv2.imwrite("ERODE_dilated3.png",orig)
#print(image)
cv2.destroyAllWindows()