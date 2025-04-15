import cv2 as cv

img = cv.imread("OpenCV/Basics/Images/Rock_melon.jpeg")

(w, h) = img.shape[:2]
aspect_ratio = h/w

custom_height = 300
custom_width = int(aspect_ratio*custom_height)

resize = cv.resize(img, (custom_width, custom_height))

print((w, h))

cv.imshow("Resized Image", resize)

cv.waitKey(0)
cv.destroyAllWindows()
