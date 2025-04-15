import cv2 as cv

# img = cv.imread("Basics/Images/Rock_melon.jpeg")
img = cv.imread("OpenCV/Basics/Images/Rock_melon.jpeg")

cv.imshow("Rock Melon", img)

cv.waitKey(0)
cv.destroyAllWindows()