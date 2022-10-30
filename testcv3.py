import cv2
import numpy as np

loc = r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/shot.png"
cv2.namedWindow("Image")
img = cv2.imread(str(loc))
cv2.imshow('/shot', img)
cv2.waitKey(5000)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

blank_image = np.zeros((500, 500, 3), dtype='uint8')
cv2.namedWindow("Blank Image")
cv2.imshow('blanl', blank_image)
cv2.waitKey(5000)
if cv2.waitKey(5000) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


def colorBg():
    ## full red
    blank_image[:] = 0, 0, 255
    cv2.imshow('full-red', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


## double
def drawLines():
    blank_image[200:300, 300:400] = 0, 0, 255
    cv2.imshow('double-color', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## rectangle inside box
    cv2.rectangle(blank_image, (0, 0), (250, 250), (0, 255, 0), thickness=2)
    cv2.imshow('Rectangle', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## circle
    cv2.circle(blank_image, (blank_image.shape[1] // 2, blank_image.shape[0] // 2), 40, (0, 255, 0), thickness=4)
    cv2.imshow('circle', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    # draw line
    cv2.line(blank_image, (0, 0), (blank_image.shape[1] // 2, blank_image.shape[0] // 2), (255, 255, 255))
    cv2.imshow('line', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


##1.5 = scale || (0,255,0) = color
def writeText():
    cv2.putText(blank_image, '[hello world]', (255, 255), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0), thickness=3)
    cv2.imshow('TEXT', blank_image)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


def picPretty():
    ## convert to grey scale
    greyScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grey Scale', greyScale)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## blur
    blur = cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT)
    cv2.imshow('blur', blur)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## edge cascade:
    cascade = cv2.Canny(blur, 125, 175)
    cv2.imshow('cascade', cascade)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

    ## dialated image
    dilated = cv2.dilate(cascade, (3, 3), iterations=1)
    cv2.imshow('dilated', dilated)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


## cv2.INTER_AREA -- faster, lower quality
## or cv2.INTER_CUBIC -- slower but higher quality

def resize(image):
    resized = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
    cv2.imshow('resized', resized)
    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


def crop(image):
    cropped = image[100:200, 200:500]
    cv2.imshow('cropped', cropped)

    cv2.waitKey(5000)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

colorBg()
drawLines()
writeText()
picPretty()
resize(img)


#
# class shapeChanger():
#     def __init__(self, loc):
#         self.cv2 = cv2.imread(str(loc))
#         self.window = cv2.namedWindow(loc)
#
#     def reSize(self):
#         resized = cv2.resize(self.cv2, (500, 500), interpolation=cv2.INTER_AREA)
#         cv2.imshow('resized by c;ass', resized)
#         cv2.waitKey(5000)
#         if cv2.waitKey(5000) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             return resized
#
#     def Crop(self):
#         cropped = self.cv2[100:200, 200:500]
#         cv2.imshow('cropped by c;ass', cropped)
#
#         cv2.waitKey(5000)
#         if cv2.waitKey(5000) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             return cropped
#
# pic_loc = r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/patric.gif"
# manip = shapeChanger(pic_loc)
# manip.reSize()
# manip.Crop()
#


# manip.reSize(colorBg())


