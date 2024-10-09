import os
import cv2
import numpy as np
from PIL import Image
import pytesseract

class ExtractEnglish:
    
    def __init__(self, image_directory):
        self.image_directory = image_directory
        self.jpg = []
        
    # 이미지 디렉토리에서 모든 JPG 파일을 수집하는 함수
    def CollectJPG(self):
        for file in os.listdir(self.image_directory):
            if file.endswith(".jpg"):
                file_path = os.path.join(self.image_directory, file)
                self.jpg.append(file_path)
        return
    
    # 전처리와 OCR 수행 함수
    def extract(self, itype):
        if itype == 'jpg':
            file_list = self.jpg
        else:
            return  # 처리할 파일이 없으면 종료
        
        for file in file_list:
            img = cv2.imread(file)
            
            if img is None:
                print(f"Unable to read {file}")
                continue
            
            # 이미지를 그레이스케일로 변환
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # 블러링 및 에지 감지
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            edged = cv2.Canny(blurred, 75, 200)

            # 이진화 (Thresholding)
            thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

            # 윤곽선 감지
            cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
            # 윤곽선을 이미지에 그리기
            cv2.drawContours(img, cnts, -1, (240, 0, 159), 3)
			
            # 이미지의 높이와 너비 가져오기
            H, W = img.shape[:2]

            # 가장 적절한 윤곽선 선택
            for cnt in cnts:
                x, y, w, h = cv2.boundingRect(cnt)
                if cv2.contourArea(cnt) > 100 and (0.7 < w/h < 1.3) and (W/4 < x + w//2 < W*3/4) and (H/4 < y + h//2 < H*3/4):
                    break

            # 마스크 생성 및 비트 연산 수행
            mask = np.zeros(img.shape[:2], np.uint8)
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            dst = cv2.bitwise_and(img, img, mask=mask)

            # 전처리된 이미지를 저장
            scanned_file_name = "output_" + str(file[:-4]) + "-Scanned.png" 
            cv2.imwrite(scanned_file_name, dst)

            # OCR 적용 후 텍스트를 추출하여 파일로 저장
            file_text = pytesseract.image_to_string(Image.open(scanned_file_name))
            text_file_name = "output_" + str(file[:-4]) + "-Scanned.txt" 
            with open(text_file_name, "a") as f:
                f.write(file_text + "\n")

if __name__ == "__main__":
    # 이미지 디렉토리를 지정하고 실행
    English = ExtractEnglish('image')
    English.CollectJPG()
    English.extract("jpg")
