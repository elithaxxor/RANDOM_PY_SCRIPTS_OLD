import cv2
import numpy as np

def stackImages(imgArray,scale,lables=[]):
    sizeW= imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver


'''Load IMG'''
path = '/Users/adelal-aali/Documents/CS/PROJECT/ssh_clients/fake/brady.png'

img = cv2.imread(path)
print(img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgStack = stackImages(([img, imgGray, imgBlur]), .06)


'''
    ** Use Cascade Methods to detect anything! (cars, face etc.) 
    ** Define Face Features 
'''


'''Display Windows '''
cv2.namedWindow('OG-Stacked')
cv2.namedWindow('OG-Grey')
cv2.namedWindow('OG')
# cv2.moveWindow('OG', (0,200,300))
# cv2.moveWindow('OG-Stacked: ', (0,200))

cv2.imshow('OG', img)
cv2.imshow('OG-Stacked', imgStack)
cv2.imshow('OG-Grey', imgGray)


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(imgGray, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)


for (x,y,w,h) in faces:
    print('X Y W H Coordinates, ', x, y,  w, h)
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

cv2.waitKey(0)
if key == ord('q') and 0xFF:
    cv2.destroyAllWindows()

