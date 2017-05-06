"""Capture video stream from webcam"""
# pylint: disable=no-member
import cv2

VIDEO = cv2.VideoCapture(0)
    
FPS = 1
while True:
    CHECK, FRAME = VIDEO.read()
    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Capturing', GRAY)
    KEY = cv2.waitKey(1)

    FPS += 1
    print(FPS)
    if ord('q') == KEY:
        break

VIDEO.release()
cv2.destroyAllWindows()
