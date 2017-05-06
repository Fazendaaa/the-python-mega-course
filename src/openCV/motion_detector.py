"""Detects motion in webcam video stream"""
# pylint: disable=no-member
import cv2

FIRST_FRAME = None
VIDEO = cv2.VideoCapture(0)
    
while True:
    CHECK, FRAME = VIDEO.read()
    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
    GRAY = cv2.GaussianBlur(GRAY, (21,21), 0)   
    
    if FIRST_FRAME is None:
        FIRST_FRAME = GRAY

    else:
        DELTA_FRAME = cv2.absdiff(FIRST_FRAME, GRAY)
        THRESH_FRAME = cv2.threshold(DELTA_FRAME, 30, 25, cv2.THRESH_BINARY)[1]
        THRESH_FRAME = cv2.dilate(THRESH_FRAME, None, iterations=2)

        (_, CNTS, _) = cv2.findContours(THRESH_FRAME.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in CNTS:
            if 1000 < cv2.contourArea(contour):
                (POS_X, POS_Y, WIDTH, HEIGHT) = cv2.boundingRect(contour)
                cv2.rectangle(GRAY, (POS_X, POS_Y), (POS_X+WIDTH, POS_Y+HEIGHT), (0, 0, 0), 3)

        cv2.imshow('Thresh Frame', THRESH_FRAME)
        cv2.imshow('Delta Frame', DELTA_FRAME)
        cv2.imshow('Gray Frame', GRAY)

        KEY = cv2.waitKey(1)

        if ord('q') == KEY:
            break

VIDEO.release()
cv2.destroyAllWindows()

