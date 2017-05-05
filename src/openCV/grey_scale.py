"""Program that reads in grey scale images and display it -- and also resize it"""
import glob
# pylint: disable=no-member
import cv2

for FILE in glob.glob('../input/*.jpg'):
    IMG = cv2.imread(FILE, 0)
    RSD_IMG = cv2.resize(IMG, (int(IMG.shape[1]/4), int(IMG.shape[0]/4)))

    cv2.imshow('Showcase', RSD_IMG)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    cv2.imwrite('../output/resized_'+FILE.split('/')[-1], RSD_IMG)

