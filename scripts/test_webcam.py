import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # settings
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
