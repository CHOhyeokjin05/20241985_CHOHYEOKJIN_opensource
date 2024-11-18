from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os
import cv2

script_dir = os.path.dirname(os.path.abspath(__file__))
# 이미지 경로
img_path = os.path.join(script_dir, 'ppocr_img/imgs/what-is-manga.jpg')

# PaddleOCR 초기화
ocr = PaddleOCR(use_angle_cls=True, lang='japan')

# 전처리 (선택 사항: 텍스트를 강조하기 위해 이미지 개선)
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    return binary

processed_img_path = os.path.join(script_dir, 'processed_image.jpg')
processed_img = preprocess_image(img_path)
cv2.imwrite(processed_img_path, processed_img)

# OCR 실행
result = ocr.ocr(processed_img_path, cls=True)

# 결과 출력
for line in result[0]:
    print(f"텍스트: {line[1][0]}, 신뢰도: {line[1][1]}")

# 결과 시각화
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result[0]]
txts = [line[1][0] for line in result[0]]
scores = [line[1][1] for line in result[0]]

# 결과를 이미지에 표시
font_path = os.path.join(script_dir, 'ppocr_img/fonts/japan.ttc') # 일본어 폰트를 지정해야 함
im_show = draw_ocr(image, boxes, txts, scores, font_path=font_path)
im_show = Image.fromarray(im_show)
im_show.save(os.path.join(script_dir, "manga_chat.jpg"))
print("결과 이미지를 저장했습니다: manga_chat.jpg")
