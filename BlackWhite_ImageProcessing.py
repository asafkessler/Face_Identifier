import cv2
cam = cv2.VideoCapture(0)
while True:
    ret, image = cam.read()
    print(image)
    gray_image = cv2.cvtColor(image,
    cv2.COLOR_BGR2GRAY)
    cv2.imshow('I AM AN IMAGE ! ',
               gray_image)
    cv2.waitKey(100)