import cv2
import numpy 

empty =cv2.imread('backgroundimage.png')
full = cv2.imread('CARS_CROPPED3.png')
empty = cv2.GaussianBlur(empty,(5,5),0)
full = cv2.GaussianBlur(full,(5,5),0)
#newimg = full-empty
#newimg = cv2.absdiff(full,empty)
newimg = cv2.bitwise_xor(full,empty)
_, car_with_shadow = cv2.threshold(newimg, 170, 255, cv2.THRESH_BINARY)
_, car_with_only_shadow = cv2.threshold(newimg, 70, 255, cv2.THRESH_BINARY)
withoutshadow = cv2.bitwise_xor(car_with_shadow,car_with_only_shadow)
_, withoutshadow = cv2.threshold(withoutshadow, 70, 255, cv2.THRESH_BINARY)
erode = cv2.erode(car_with_only_shadow,None,iterations=1)
cv2.imshow('shadowremoved',withoutshadow)
cv2.imshow('only shadow',car_with_only_shadow)
cv2.imshow('car with shadow',car_with_shadow)
cv2.imshow('original',erode)
cv2.imshow("fa",full)
cv2.imwrite("ERODE4.png",withoutshadow)
cv2.waitKey()
cv2.destroyAllWindows()