import cv2
from HackendUtils import face_recognition as fr

my_face_classifier = fr.get_face_detector()
camera = cv2.VideoCapture(0)
BLUE = (255, 0 ,0)

while True:
    ret, image = camera.read()
    faces = fr.detect(my_face_classifier, image)
    for (x, y, w, h) in faces:
        cv2.circle(image, (x + int(h/2), y + int(w/2)), int(h/2), BLUE, 10)
    cv2.imshow('NEVER STOP DREAMING : (AsafKessler & ScienceMuseum)', image)
    cv2.waitKey(10)


#1. call the face classifier
#2. connect to camera
#3. show live video
#4. understand what is face
#5. draw a rectangle with the chosen color around the face