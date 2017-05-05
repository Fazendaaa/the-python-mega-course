"""Detects and returns it a image with face detection"""
# pylint: disable=no-member
import cv2

FACE_CASCADE = cv2.CascadeClassifier('../input/haarcascade_frontalface_default.xml')

IMG = cv2.imread('../input/baby-933097.jpg')
IMG = cv2.resize(IMG, (int(IMG.shape[1]/4), int(IMG.shape[0]/4)))
GRAY_IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)

FACES = FACE_CASCADE.detectMultiScale(GRAY_IMG, scaleFactor=1.05, minNeighbors=5)

for START_X, START_Y, WIDTH, HEIGHT in FACES:
    # pylint: disable=line-too-long
    FACE_IMG = cv2.rectangle(GRAY_IMG, (START_X, START_Y), (START_X+WIDTH, START_Y+HEIGHT), (0, 0, 0), 3)

cv2.imshow('Gray', FACE_IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('../output/baby-933097.jpg', FACE_IMG)
