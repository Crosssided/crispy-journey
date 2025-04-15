import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame = cap.read()

h, w = frame.shape[:2]
aspect_ratio = w/h

height = 400
width = int(height*aspect_ratio)

while True:
    ret, frame = cap.read()
    frame = cv.Canny(frame, 50, 100)
    frame = cv.flip(frame, 1)

    if not ret:
        break
    frame_resized = cv.resize(frame, (width, height))

    cv.imshow("Webcam", frame_resized)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
