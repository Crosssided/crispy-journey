import cv2 as cv

# img = "Basics/Images/Rock_melon.jpeg"
img = cv.imread("OpenCV/Basics/Images/Rock_melon.jpeg")

(h, w) = img.shape[:2]
aspect_ratio = w/h
resized_h = 400
resized_w = int(resized_h*aspect_ratio)

scaling = cv.resize(img, (resized_w, resized_h))

# grayscale
grayscale = cv.cvtColor(scaling, cv.COLOR_BGR2GRAY)
# blur
blurred = cv.GaussianBlur(scaling, (21, 21), 0)
# edge detection
edge = cv.Canny(scaling, 100, 200)
# image, threshold 1, threshold 2.
# pixels with a lower gradient than threshold 1 are ignored
# pixels with a higher gradient that threshold 2 are strong edges
# pixels between these 2 are weak edges and are shown if connected to a strong edge

# A gradient in an image measures how fast pixel intensity (brightness) changes from one pixel to another. It helps detect edges, which are areas where this intensity changes sharply.

cv.imshow("Image Grayscale", grayscale)
cv.imshow("Image Blurred", blurred)
cv.imshow("Image edges", edge)

cv.waitKey(0)
cv.destroyAllWindows()