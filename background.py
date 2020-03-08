import cv2 
import time
cap = cv2.VideoCapture("highway.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)
i=0
while True:
    r, frame = cap.read()
    #print(reyt)
    if r == True:
        frame = cv2.resize(frame,(300,300))
        mask = subtractor.apply(frame)
        
        cv2.imshow('Frame',mask)
        cv2.imwrite('masked{}.png'.format(i),mask)
        i+=1
        x = cv2.waitKey()
    elif x == 27:
        break
    else:
        pass
    
cap.release()
cv2.destroyAllWindows()