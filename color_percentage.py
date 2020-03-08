import cv2 
import numpy as np
#img_name = input("What's the name of the picture? ")
img = cv2.imread('erode_dilated3.png')
original = cv2.imread("CARS_CROPPED3.png")
#img = img[50:,:]
# boundaries for the color red
boundaries = [
    ([150, 150, 150], [255, 255, 255])
    ]
for(lower, upper) in boundaries:
    # creates numpy array from boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # finds colors in boundaries a applies a mask
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)
    # saves the image  #cv2.imwrite('2', output)
    cv2.imshow('js',img)
    cv2.waitKey(0)
tot_pixel = output.size
print(img.shape,output.shape)
red_pixel = np.count_nonzero(output)
percentage = round(red_pixel * 100 / tot_pixel, 2)

print("WHITE pixels: " + str(red_pixel))
print("Total pixels: " + str(tot_pixel))
print("Percentage of WHITE pixels: " + str(percentage) + "%")
print("NON OCCUPANCY OF THE ROAD IS: "+str(100-percentage)+"%")
vehicle_count = 100-percentage
if vehicle_count <=40:
    print("---------RUNNING 40 -----------")
    cv2.circle(original,(90,100),40,(0,0,255),-1)
    
    cv2.putText(original," ROAD NON OCCUPANCY IS "+str(vehicle_count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
elif vehicle_count <=70:
    
    print("---------RUNNING 60 -----------")
    cv2.circle(original,(90,100),40,(52,25,48),-1)
    
    cv2.putText(original," ROAD NON OCCUPANCY IS "+str(vehicle_count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(52,25,48),2)

else:
    
    print("---------RUNNING 80 -----------")
    cv2.circle(original,(90,100),40,(255,0,0),-1)
    
    cv2.putText(original,"ROAD NON OCCUPANCY IS "+str(vehicle_count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
print("0-40 ==> RED "," 41-70==> PURPLE ","71-100 ==> BLUE")
print(vehicle_count)
cv2.imshow("ORIGINAL",original)
#cv2.imwrite("New folder/vehicle_count1.png",original)
cv2.waitKey(0)
cv2.destroyAllWindows()