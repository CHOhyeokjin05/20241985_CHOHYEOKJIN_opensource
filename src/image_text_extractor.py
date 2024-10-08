import os
import cv2
import numpy as np
from PIL import Image
import pytesseract

# Update the path to your actual directory
image_directory = "/home/jin/Text-Extraction-From-Image/set10"

# exploring the directory for all jpg files
for file in os.listdir(image_directory):
    if file.endswith(".jpg"):
        file_path = os.path.join(image_directory, file)
        img = cv2.imread(file_path)
        ratio = img.shape[0] / 500.0
        original_img = img.copy()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Blurring and finding edges
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)

        # Thresholding
        thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

        # Finding contours (correct return unpacking)
        cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        # draw contours on image 
        cv2.drawContours(img, cnts, -1, (240, 0, 159), 3)

        H,W = img.shape[:2]
        for cnt in cnts:
            x,y,w,h = cv2.boundingRect(cnt)
            if cv2.contourArea(cnt) > 100 and (0.7 < w/h < 1.3) and (W/4 < x + w//2 < W*3/4) and (H/4 < y + h//2 < H*3/4):
                break

        # creating mask and performing bitwise-op
        mask = np.zeros(img.shape[:2],np.uint8)
        cv2.drawContours(mask, [cnt],-1, 255, -1)
        dst = cv2.bitwise_and(img, img, mask=mask)

        # displaying image and saving in the directory
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        scanned_file_name = "set10/" + str(file[:-4]) + "-Scanned.png" 
        cv2.imwrite(scanned_file_name, dst)
        # cv2.imshow("gray.png", dst)
        # cv2.waitKey()

        # fetching text from the image and storing it into a text file
        file_text = pytesseract.image_to_string(Image.open(scanned_file_name))
        text_file_name = "set10/" + str(file[:-4]) + "-Scanned.txt" 
        with open(text_file_name, "a") as f:
            f.write(file_text + "\n")
        # import pdb; pdb.set_trace()