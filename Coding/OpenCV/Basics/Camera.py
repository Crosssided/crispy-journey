import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame = cap.read() # ret is a boolean value.

# resize
h, w = frame.shape[:2]
aspect_ratio = w/h

frame_height = 400
frame_width = int(frame_height * aspect_ratio)

while True:
    ret, frame = cap.read()
    
    frame = cv.flip(frame, 1) # 1 is for flipping vertically, 0 is flipping horizontally

    if not ret:
        break

    frame_resized = cv.resize(frame, (frame_width, frame_height)) # resize takes 3 arguments: frame, (width, height)
    cv.imshow("Webcam", frame_resized)

    # break loop if q is pressed. ord gets the ascii value since waitkey takes an interger value.
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()