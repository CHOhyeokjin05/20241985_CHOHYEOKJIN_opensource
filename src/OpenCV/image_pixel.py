import cv2
import os
import numpy as np

image_path = os.path.join(os.path.dirname(__file__), "../PaddleOCR/ppocr_img/imgs_en/img_12.jpg")
img = cv2.imread(image_path, 0)

height, width = img.shape

print(height, width)



for j in range( height//2, height):
    for i in range(width):
        img[174,i] = 0
cv2.imshow('sample', img)
cv2.waitKey()
cv2.destroyAllWindows()