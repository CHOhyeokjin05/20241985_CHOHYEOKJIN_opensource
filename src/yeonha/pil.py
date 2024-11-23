# 직사각형 생성

from paddleocr import PaddleOCR, draw_ocr
import os
from PIL import Image, ImageDraw, ImageFont

# 현재 스크립트의 경로
script_dir = os.path.dirname(os.path.abspath(__file__))

# PaddleOCR 초기화
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # 영어 모델 사용
img_path = os.path.join(script_dir, 'ppocr_img/imgs_en/img_12.jpg')  # 이미지 경로
result = ocr.ocr(img_path, cls=True)  # OCR 실행

# OCR 결과 출력
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 결과 그리기
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result[0]]
txts = [line[1][0] for line in result[0]]
scores = [line[1][1] for line in result[0]]

# 이미지에 OCR 결과 박스 표시
im_show = draw_ocr(image, boxes, txts, scores, font_path=os.path.join(script_dir, 'ppocr_img/fonts/simfang.ttf'))
im_show = Image.fromarray(im_show)

# 하단에 텍스트 직사각형 추가
draw = ImageDraw.Draw(im_show)
font_path = os.path.join(script_dir, 'ppocr_img/fonts/simfang.ttf')  # 폰트 파일 경로
font = ImageFont.truetype(font_path, size=20)  # 텍스트 폰트 크기 설정

# 추출된 텍스트 합치기
extracted_text = "\n".join(txts)  # 여러 줄로 표시

# 직사각형 크기 계산
rect_height = 100  # 직사각형 높이
image_width, image_height = im_show.size
rectangle = [(0, image_height), (image_width, image_height + rect_height)]

# 직사각형 그리기
draw.rectangle(rectangle, fill="white", outline="black")

# 텍스트 추가
draw.text((10, image_height + 10), extracted_text, fill="black", font=font)

# 결과 저장
output_path = os.path.join(script_dir, 'result_with_text.jpg')
im_show.save(output_path)
print(f"결과 이미지가 저장되었습니다: {output_path}")
