import numpy as np
import cv2

# mode = "image"
mode = "webcam"
outlet_cascade = cv2.CascadeClassifier('./classifier/cascade.xml')

if mode=="image":
    img = cv2.imread('test_outlet.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    outlets = outlet_cascade.detectMultiScale(gray, 1.1, 2, minSize=(24,24))
    for (x,y,w,h) in outlets:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)
    cv2.imwrite('test_outlet_result.jpg', img)
    cv2.waitKey(0)

if mode=="webcam":
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, img = video_capture.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        outlets = outlet_cascade.detectMultiScale(gray, 1.2, 10, minSize=(10,10))
        for (x,y,w,h) in outlets:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()