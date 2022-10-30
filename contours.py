import cv2, sys, os
import numpy as np

''' 
        * find contours #1
        * use for loop to find area inbeteeen contours. #2
         * create box and object around arc perimter / approximation... CHANGE AREA  #3
         * use cv2.rectangle to draw box around approxmation #4
'''
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



def getContours(img): #1
    difference = cv2.absdiff(img, imgBlur)
    _, thresh = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    contours, hiearchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Get the threshold of the difference between the two frames


    for find_area in contours: #2
        area = cv2.contourArea(find_area)
        print('AREA', area)

        if area > 50: #3
            cv2.drawContours(img, find_area, -1,(255,0,0),3) ## drraw on to the copy of image, rather than original,
            arc_perimeter = cv2.arcLength(find_area, True)
            approx = cv2.approxPolyDP(find_area, 0.02* arc_perimeter, True)
            print('arc_perimeter', arc_perimeter)
            print('Approximation', approx)
            ## 4
            x, y, w, h = cv2.boundingRect(approx)
            objCor = len(approx)
            print('objCor',objCor)
            print('bounding rectangle coordinates,', x,y,w,h)

            if objCor == 3: ## triangle
                objectType = "tri"
                print('Object Detected, ', objectType)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            elif objCor == 4:
                aspRatio = float(w) / float(h)
                if aspRatio > .95 and aspRatio < 1.05:  ## allows 5% error
                    objectType = "square" # if anything is within 5% of ^
                    print('Object Detected, ', objectType)
                else:
                    objectType = "Rectangle"
                    print('Object Detected, ', objectType)
            elif objCor > 4:
                objectType = 'circles'
                print('Object Detected, ', objectType)
            else:
                objectType = 'None'
                print('Object Detected, ', objectType)

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,255,255),2)

            #cv2.putText(img, (x + (w // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, .05, (0, 255, 255), 2)
            cv2.namedWindow('Contour Image With Shape Detection:')
            cv2.moveWindow('Contour Image With Shape Detection:', 700, 100)
            cv2.imshow('Contour Image With Shape Detection:', img)
            cv2.imshow('Contour Image With Shape Detection:', thresh)




path = r"/Users/adelal-aali/Documents/CS/PROJECT/ssh_clients/batman.jpg"


img = cv2.imread(str(path))
imgContour_COPY = img.copy()


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),cv2.BORDER_DEFAULT)



'''find edges in image'''
imgCanny = cv2.Canny(imgBlur,50,50)

'''Create stacked image'''
''' Stacking images without Function '''


#
#
# imgBlur = cv2.resize(img, (0, 0), None, 0.5, 0.5)
# imgGray = cv2.resize(imgGray, (0, 0), None, 0.5, 0.5)
# hor = np.hstack((imgBlur, imgGray))
# ver = np.vstack((imgGray, imgBlur))
# cv2.imshow('Vertical', ver)
# cv2.imshow('Horizontal', hor)
# cv2.waitKey(0)
#


''' STACKING WITH FUNCTION '''
getContours(imgCanny)

imgBlank = np.zeros_like(img)
StackedImages = stackImages(([img,imgGray,imgBlank],
                             [imgCanny,imgBlur,imgBlank]),.06)




cv2.imshow('stack', StackedImages)
cv2.imshow('original', img)
cv2.imshow('grey', imgGray)
cv2.imshow('blur', imgBlur)
cv2.imshow('cany', imgCanny)



if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    img.release()










