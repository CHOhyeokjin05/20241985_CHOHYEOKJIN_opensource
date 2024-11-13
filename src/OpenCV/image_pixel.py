import cv2
import os
import numpy as np

image_path = os.path.join(os.path.dirname(__file__), "../PaddleOCR/ppocr_img/imgs_en/img_12.jpg")
img = cv2.imread(image_path, 0)

height, width = img.shape

print(height, width)

data = [[[[441.0, 174.0], [1166.0, 176.0], [1165.0, 222.0], [441.0, 221.0]], ('ACKNOWLEDGEMENTS', 0.9974855780601501)], 
        [[[403.0, 346.0], [1204.0, 348.0], [1204.0, 384.0], [402.0, 383.0]], ('We would like to thank all the designers and', 0.9683309197425842)], 
        [[[403.0, 396.0], [1204.0, 398.0], [1204.0, 434.0], [402.0, 433.0]], ('contributors who have been involved in the', 0.9776103496551514)], 
        [[[399.0, 446.0], [1207.0, 443.0], [1208.0, 484.0], [399.0, 488.0]], ('production of this book; their contributions', 0.9866490960121155)], 
        [[[401.0, 500.0], [1208.0, 500.0], [1208.0, 534.0], [401.0, 534.0]], ('have been indispensable to its creation.We', 0.9628525972366333)], 
        [[[399.0, 550.0], [1209.0, 548.0], [1209.0, 583.0], [399.0, 584.0]], ('would also like to express our gratitude to all', 0.9740485548973083)], 
        [[[399.0, 600.0], [1207.0, 598.0], [1208.0, 634.0], [399.0, 636.0]], ('the producers for their invaluable opinions', 0.9963331818580627)], 
        [[[399.0, 648.0], [1207.0, 646.0], [1208.0, 686.0], [399.0, 688.0]], ('and assistance throughout this project. And to', 0.9943731427192688)], 
        [[[399.0, 702.0], [1209.0, 698.0], [1209.0, 734.0], [399.0, 738.0]], ('the many others whose names are not credited', 0.9772290587425232)], 
        [[[399.0, 750.0], [1211.0, 750.0], [1211.0, 789.0], [399.0, 789.0]], ('but have made specific input in this book, we', 0.997929036617279)], 
        [[[397.0, 802.0], [1090.0, 800.0], [1090.0, 839.0], [397.0, 841.0]], ('thank you for your continuous support.', 0.9981997609138489)]]




for idx in range(len(data)):
    for line in data[idx]:
        img[line[0]] = 0
cv2.imshow('sample', img)
cv2.waitKey()
cv2.destroyAllWindows()