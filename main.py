from turtle import width
import cv2

cam = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade_side = cv2.CascadeClassifier("haarcascade_profileface.xml")

while True:
    _, im = cam.read()
    im_grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(im_grey)
    side = cascade_side.detectMultiScale(im_grey)
    for x,y, width, height in faces:
        cv2.rectangle(im, (x, y), (x + width, y + height), color=(255,0,0), thickness=4)
        cv2.rectangle(im_grey, (x,y), (x + width, y+ height), color=(0,255,0), thickness=4)
    cv2.imshow("Kamera", im)
    cv2.imshow("S/W Cam", im_grey)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows