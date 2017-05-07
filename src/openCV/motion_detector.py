"""Detects motion in webcam video stream"""
from datetime import datetime
# pylint: disable=no-member, multiple-imports
import cv2, pandas

TIMES = []
STATUS_LIST = [None, None]
DF = pandas.DataFrame(columns=['Start', 'End'])

FIRST_FRAME = None
VIDEO = cv2.VideoCapture(0)

while True:
    STATUS = 0
    CHECK, FRAME = VIDEO.read()
    GRAY = cv2.cvtColor(FRAME, cv2.COLOR_BGR2GRAY)
    GRAY = cv2.GaussianBlur(GRAY, (21, 21), 0)

    if ord('q') == cv2.waitKey(1):
        # pylint: disable=misplaced-comparison-constant
        if 1 == STATUS:
            TIMES.append(datetime.now())
        break

    if FIRST_FRAME is None:
        FIRST_FRAME = GRAY

    else:
        DELTA_FRAME = cv2.absdiff(FIRST_FRAME, GRAY)
        THRESH_FRAME = cv2.threshold(DELTA_FRAME, 30, 25, cv2.THRESH_BINARY)[1]
        THRESH_FRAME = cv2.dilate(THRESH_FRAME, None, iterations=2)

        # pylint: disable=line-too-long
        (_, CNTS, _) = cv2.findContours(THRESH_FRAME.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in CNTS:
            # pylint: disable=misplaced-comparison-constant
            if 1000 < cv2.contourArea(contour):
                STATUS = 1
                (POS_X, POS_Y, WIDTH, HEIGHT) = cv2.boundingRect(contour)
                cv2.rectangle(FRAME, (POS_X, POS_Y), (POS_X+WIDTH, POS_Y+HEIGHT), (0, 255, 0), 3)

        STATUS_LIST.append(STATUS)
        STATUS_LIST = STATUS_LIST[-2:]

        if STATUS_LIST[-1] != STATUS_LIST[-2]:
            TIMES.append(datetime.now())

        cv2.imshow('Thresh Frame', THRESH_FRAME)
        cv2.imshow('Delta Frame', DELTA_FRAME)
        cv2.imshow('Gray Frame', GRAY)
        cv2.imshow('Color Frame', FRAME)


for INDEX in range(0, len(TIMES), 2):
    DF = DF.append({'Start': TIMES[INDEX], 'End': TIMES[INDEX+1]}, ignore_index=True)

DF.to_csv('../output/Times.csv')

VIDEO.release()
cv2.destroyAllWindows()
