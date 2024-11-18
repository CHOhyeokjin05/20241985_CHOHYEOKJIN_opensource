import os
import sys
import PIL.Image
from manga_ocr import MangaOcr


# export PYTHONPATH=$PYTHONPATH:/home/jin/20241985/src/manga-ocr-master
# 모듈을 찾기 위해서 위 문구 실행


# # 절대 경로로 변환 -> 작동 안 함
# project_path = os.path.expanduser('~/20241985/src/manga-ocr-master')
# sys.path.append(project_path)

mocr = MangaOcr()
img = PIL.Image.open('tests/data/images/01.jpg')

# OCR 실행
text = mocr(img)

# 결과 저장
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
