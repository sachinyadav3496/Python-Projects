import cv2
import pytesseract
import numpy as np
from PIL import Image
def handle_uploaded_file(f):
    with open('static/test.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    img_path = 'static/test.jpg'
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite("C:\\Users\\sachin yadav\\Desktop\\TextExtractor\\static\\removed_noise.png", img)
    cv2.imwrite("C:\\Users\\sachin yadav\\Desktop\\TextExtractor\\static\\new.png", img)
