import cv2, time, datetime, imutils
from cv2 import cv2
import numpy as np
from datetime import date

'''
pip3 install opencv-python
1. set greyscale frame 
2. set image kernal to 21x2 grid,
3. blur screen in smaller frame 
4. set condition to keep greyscale blurred 
5. $$ set logic for video capture if frame is presented $$
6. resize frame after condition is met 
7. use cv2.absdiff to find difference between greyscale img and recorded frame  
8. apply cv2.thresholding to seperate background image from foreground image 

## thresholding is the binazation of images. Converts greyscale back to binary (px 0 or 255)
## use to seperate forground and backgorund imagse 
'''

'''
:: SAMPLE BASIC THRESHOLDING :: 
1. CONVERT TO GREYSCALE
2. APPLY 7X7 GAUSSIAN BLUR 
3. APPLY THRESHILD
## FIRST PARAMETER IS IMAGE, 2ND IS 'THRESHOLD CHECK' 
## IF PIXLE IS GREATER THAN 200, SET TO BLACK 
## ELSE SET IT TO WHITE 

image = cv2.imread(args["image"])
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
(T, threshInv) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
(T, threshInv) = cv2.threshold(blurred, 200, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

CONTOURS GIVE DIFFERNT OUTPUTS (IMAGE, CONTOUR AND ARCHY. THE CONTOUR IS SET TO BLUE 
CV2.CHAIN_APPROX_SIMPLE REMOVES REDUNDENCY AND COMPRESSES IMAGE 
SET CONDITION, IF CONTOURAREA  IS LARGER THAN 800 

'''


def motion_detection():
    video_capture = cv2.VideoCapture(0)
    time.sleep(2)
    first_frame = None
    while True:
        frame = video_capture.read()[1]
        text = f'undetected{time.ctime()}'
        greyscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gaussian_frame = cv2.GaussianBlur(greyscale_frame,(21,21),0)
        blur_frame = cv2.blur(gaussian_frame, (5,5),0) ## blurs pictures with 5x5 image kernal
        greyscale_image = blur_frame

        if first_frame is None:
            first_frame = greyscale_image
        else:
            pass
        frame = imutils.resize(frame, width=500)
        frame_delta = cv2.absdiff(first_frame, greyscale_image)
        thresh = cv2.threshold(frame_delta, 100, 255, cv2.THRESH_BINARY)[1] ## once the frame is over 100, we make it white
        dilate_image = cv2.dilate(thresh, None, iterations=2) # enlarge and expand white pixle in forgroudn
        _,cnt, _= cv2.findContours(dilate_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ## OPENCV 3
        #cnt,_= cv2.findContours(dilate_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ## OPENCV 4

        for c in cnt:
            (x, y, w, h) = cv2.boundingRect(c)
            #(x, y, w, h) = cv2.boundingRect(contour.astype(np.int))

            if cv2.contourArea(c) > 800:
                (x,y,w,h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) ## draw green box around object (set security feed frame)

                text = f'[Detected] {time.ctime()} || {date.today()} '
                with open('camera_log.txt', 'a') as f:
                    f.write(text)
            else:
                pass

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, f'Room Status: {text}', (10,20),font,0.5,(0,0,255),2)
            cv2.putText(frame, f'Time: {time.ctime()}', (10, frame.shape[0]-10),font,0.35,(0,0,255),1)
            cv2.imshow('[Security Feed]', frame)
            cv2.imshow('Threshold [Front-IMage]', dilate_image)
            cv2.imshow('Frame_Delta,', dilate_image)
            key=cv2.waitKey(1) & 0xFF ## 0xFF hex constant
            if key == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == '__main__':
    motion_detection()




