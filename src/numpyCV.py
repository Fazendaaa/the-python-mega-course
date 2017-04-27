import numpy
import cv2

n = numpy.arange( 27 )
print( n, "\n" )
print( n.reshape( 3, 9 ), "\n" )
print( n.reshape( 3, 3, 3 ), "\n" )

im_g = cv2.imread( "./input/smallgray.png", 0 )
print( im_g, "\n" )

cv2.imwrite( "./output/newSmallgray.png", im_g )

#   concatenating arrays
#       h = horizontal
#       v = vertical
im_ch = numpy.hstack( ( im_g, im_g, im_g ) )
im_cv = numpy.vstack( ( im_g, im_g, im_g ) )
print( im_ch, "\n\n", im_cv, "\n" )

#   spliting arrays
im_sh = numpy.hsplit( im_cv, 5 )
im_sv = numpy.vsplit( im_cv, 3 )
print( im_sh, "\n\n", im_sv, "\n" )

#   ------------------------------   EOF   ---------------------------------   #
