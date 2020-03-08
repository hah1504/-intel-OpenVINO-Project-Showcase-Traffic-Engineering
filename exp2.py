import numpy as np
import cv2
#import imutils

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
image = cv2.imread('dilated.png',0)
original = cv2.imread("foregroundimage.png")
#---- removing the noise 
#Gimg  = cv2.GaussianBlur(image,(7,7),0)
#image = cv2.erode(image,None,iterations=1)
#image = cv2.dilate(image,None,iterations=1)

#cv2.imshow("erode",image)
#cv2.waitKey(0)
#image = image[50:,:]
vehicle_count=0

#image = cv2.dilate(image,None,iterations=8)
#cv2.imshow("dilated",image)
#cv2.imwrite("dilated.png",image)
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
    
#ximg = cv2.dilate(orig,None,iterations=2)
#cv2.imshow("DILATION",ximg)
cv2.waitKey(0)
cv2.drawContours(orig,multiple_contours,-1,(139,131,255),2)
cv2.putText(orig,str(vehicle_count),(10,90),cv2.FONT_HERSHEY_COMPLEX,1,(139,131,255),2)
cv2.putText(original,str(vehicle_count),(10,90),cv2.FONT_HERSHEY_COMPLEX,1,(139,131,255),2)
if vehicle_count <=40:
    print("---------RUNNING 40 -----------")
    cv2.circle(original,(90,100),40,(0,0,255),-1)
elif vehicle_count <=70:
    
    print("---------RUNNING 60 -----------")
    cv2.circle(original,(90,100),40,(52,25,48),-1)
else:
    
    print("---------RUNNING 80 -----------")
    cv2.circle(original,(90,100),40,(255,0,0),-1)
print("0-40 ==> RED "," 41-70==> PURPLE ","71-100 ==> BLUE")
cv2.imshow("ORIGINAL",original)

cv2.imshow("IMAGE",orig)
cv2.waitKey(0)
cv2.imwrite("New folder/vehicles_count1.png",original)
#print(image)
cv2.destroyAllWindows()