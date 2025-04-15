import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame = cap.read()

h, w = frame.shape[:2]
aspect_ratio = w/h

# original: w=1200, h=800
# resized: w=600 h=800*600/800

width = 600
height = int(width*aspect_ratio)


while True:

    ret, frame = cap.read()

    greyscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.flip(greyscale, 1)

    resized_frame = cv.resize(frame, (height, width))

    if not ret:
        break

    if cv.waitKey(1) == ord("q"):
        break

    cv.imshow("Webcam", resized_frame)


cap.release()
cv.destroyAllWindows()