import cv2

def image_parser(loc):
    cv2.namedWindow("Image")
    img = cv2.imread(str(loc))
    cv2.imshow('/shot', img)
    cv2.waitKey(5000)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        return loc, img
    cv2.destroyAllWindows()
    return loc, img

### add _large behind .png to make larger
def expand_image(img):
    cv2.namedWindow("Image2")
    img_large = cv2.imread(img)
    cv2.imshow('/shot', img_large)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

def display_video(vid):
    global capture
    capture = cv2.VideoCapture(vid)
    tf = capture.isOpened()
    if tf == False: capture.open(vid)
    while True:
        isTrue, frame = capture.read()
        print(f'[+] frame True? [{isTrue}] :: [{tf}]')
        cv2.imshow('video', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'): return frame
        capture.release()
        cv2.destroyAllWindows()
        return frame, capture

def live_capture():
    global capture
    capture = cv2.VideoCapture(0)
    tf = capture.isOpened()
    #if tf == False: capture.open()
    while True:
        isTrue, frame = capture.read()
        print(f'[+] frame True? [{isTrue}] :: [{tf}]')
        cv2.imshow('video', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'): return frame
        capture.release()
        cv2.destroyAllWindows()
        return frame, capture


## works best for existing video / streams
# also works for videos, images and webcam
def rescaleFrames(frame, scale=1.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height) # set tuple for return
    print(f'[+] Dimensions :: [{width}] x [{height}] :: [+]')
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

## only works for webcam
def rescaleRes(frame, scale=1.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    capture.set(3, width)  ## key 3 represients teh width
    capture.set(4, height) ## key 4 represents height


## live capture
vid, feed = live_capture()
rescale_feed = rescaleRes(vid)

## image parser and resizing
img_loc = r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/shot.png"
loc, frame = image_parser(img_loc)
resize_image = rescaleFrames(frame)
resized_image = image_parser(img_loc) ## make it into a class for inhertiane. functionality is a pain the the ass

## video parser and resizing
vid_loc = "/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/random.mp4"
orig_vid, cap = display_video(vid_loc)
resize_vid = rescaleFrames(orig_vid)
rescale_res = rescaleRes(orig_vid)
resized_video = display_video(vid_loc)




