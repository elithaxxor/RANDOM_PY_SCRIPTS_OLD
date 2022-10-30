import cv2, math, traceback, sys, os
import numpy as np
from cvzone.HandTrackingModule import HandDetector

'''
    * Create trackbar 
    * namedWindow 
    * createTrackbar, [str], [namedWindow], [min val] [max val], []
'''

def empty():
    pass


'''SET BLANK IMAGE'''
img = np.zeros((512,512,3),np.uint8)
print(img)
cv2.namedWindow('BLANK-IMG')
cv2.moveWindow('BLANK-IMG', 300,300)

'''
    * draw line on image
    * heightm then width ,(img.shape[1],img.shape[0])
'''
'''
    * rectangle
    * starting point(0,0) 
    * endinng point (300, 300)
    * colo green
    * thickness ,3 or fill rectange
'''
cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(300, 350), (0,0,255),3)
cv2.rectangle(img,(0,0),(300, 350), (0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img, " OPEN CV ",(300,200), cv2.FONT_HERSHEY_DUPLEX,2.0,(0,150,0),3)
cv2.imshow('BLANK-IMG', img)

'''  
    * Importing image and getting pictures pulled out of them. 
    * 
'''
cv2.namedWindow('picture removal')
width, height = 250, 350
img_import = cv2.imread('cards.jpeg')
pts1 = np.float32([[425, 6], [696, 167], [461, 633], [167, 702]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
print('imported image shape', img_import.shape)
print(img_import)

print('PTS1 Empty npfloat32 for card ARRAY: \n', pts1)
print('PTS1 card SHAPE: \n', pts1.shape)
print('PTS2 Empty npfloat32 for card ARRAY: \n', pts2)
print('PTS2card SHAPE: \n', pts2.shape)

''' matrix - then warperpsecgive'''
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img_import, matrix, (width, height))
cv2.imshow('picture removal', imgOut)

if cv2.waitKey(0) & 0xFF:
    cv2.destroyAllWindows()



cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera in use')
    sys.exit(1)
'''Retrieve Frame Height.'''
print('Frame Height')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
'''Reset Frame Height'''
print('New Frame Dimensions')
cap.set(3, 1280)
cap.set(4, 720)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
'''Set camera brightness'''
cap.set(10,100)

# hand detector:
detector = HandDetector(detectionCon=.8, maxHands=1)
''' Use Media Pipe to find distance aunder detector.findHands'''

'''
    * Create empty picture array for dilate 
    * Dilate increases the thickness drawn around the image 
    * CANNY-EDGE-DETECTION - 100x100 is threshold level 
    * Increase Thickness by iterations=
    *** cv2.dilate to dilate || cv2.erode to make less thick ****
'''

kernal = np.ones((5,5),np.uint8)
print(kernal)

while True:
    cv2.namedWindow('[+] ORIG-SLIDE')
    cv2.namedWindow('[+] Trackbar-SLIDE')
    cv2.namedWindow('[+] MASK')
    cv2.resizeWindow('[+] Trackbar-SLIDE', 640, 320)

    cv2.namedWindow('[+] Combined With Mask')

    cv2.createTrackbar('Hue Min', 'Trackbar-SLIDE', 0, 179, empty)
    cv2.createTrackbar('Hue Max', 'Trackbar-SLIDE', 19, 179, empty)
    cv2.createTrackbar('Sat Min', 'Trackbar-SLIDE', 110, 255, empty)
    cv2.createTrackbar('Sat Max', 'Trackbar-SLIDE', 240, 255, empty)
    cv2.createTrackbar('Val Min', 'Trackbar-SLIDE', 153, 255, empty)
    cv2.createTrackbar('Val Max', 'Trackbar-SLIDE', 255, 255, empty)

    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbar-SLIDE')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbar-SLIDE')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbar-SLIDE')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbar-SLIDE')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbar-SLIDE')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbar-SLIDE')

    cv2.namedWindow('[+] Tracking Frame')
    cv2.namedWindow('[+] Tracking Frame blur')
    cv2.namedWindow('[+] Tracking Frame canny')
    cv2.namedWindow('[+] Tracking Frame eroded')

    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print('frameshape \n', frame.shape)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    ret_slider, img_slider = cap.read()
    mask = cv2.inRange(img_slider, lower, upper)
    combined_images = cv2.bitwise_and(frame,frame,mask=mask)
    #cv2.imshow('Trackbar-SLIDE', Trackbar-SLIDE)
    ''' stacking images'''
    # img img_import -
    imgStack = stackImages(0.6, ([frame, ret_slider], [mask, combined_images]))

    if not ret_slider:
        print('could not open slider'); pass
    slide_frame = cv2.cvtColor(img_slider, cv2.COLOR_RGB2LUV)
    print(h_min, h_max, s_max, s_min, v_min, v_max)

    cv2.imshow('imgStack', imgStack)
    pring('imgStak-Size', imgStack.size)

    cv2.imshow('[+] ORIG-SLIDE', img_slider)
    cv2.imshow('[+] Trackbar-SLIDE', slide_frame)
    cv2.imshow('[+] MASK', mask)
    cv2.imshow('[+] Combined With Mask', combined_images)

    flag, img = cap.read()
    print('frameshape \n', img.shape)
    img = cv2.resize(img,(500,500))
    print('frameshape \n', img.shape)


    setGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    setBlur = cv2.GaussianBlur(setGrey, (7,7),0)
    imgCanny = cv2.Canny(img,100,100)
    imgDialation = cv2.dilate(imgCanny,kernal,iterations=1) ## iterations
    imgErod = cv2.erode(imgDialation,kernal,iterations=2)


    if not ret:
        print('Unable to recv stream')
        break
    print(ret)
    hands, frame = detector.findHands(frame)
    if hands:
        lmList = hands[0]['lmList']
        x1, y1 = lmlist[5] # sets to index knucke, point 5 (index 5-8)
        x2, y2 = lmlist[17]  # set index to pinky knickle (pinky 17-20)
        distance = int(math.sqrt((y2-y1) **2 + (x2-x1) **2))
        print(distance)
        print(y1)

    cv2.imshow('[+] Tracking Frame', frame)
    cv2.imshow('[+] Tracking Frame blur', setBlur)
    cv2.imshow('[+] Tracking Frame canny', imgCanny)
    cv2.imshow('[+] Tracking Frame eroded', imgErod)

    if cv2.waitKey(0) & 0xFF:
        cap.release()
        cv2.destroyAllWindows()
        break



