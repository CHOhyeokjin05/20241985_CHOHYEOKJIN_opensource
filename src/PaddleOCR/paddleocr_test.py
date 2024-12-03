from paddleocr import PaddleOCR,draw_ocr
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = os.path.join(script_dir, 'ppocr_img/imgs_en/img_12.jpg')
# ocr = PaddleOCR(use_angle_cls=True, lang='japan')
# img_path = os.path.join(script_dir, 'ppocr_img/imgs_en/img_12.jpg')
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path=os.path.join(script_dir,'ppocr_img/fonts/simfang.ttf'))
im_show = Image.fromarray(im_show)
im_show.save(os.path.join(script_dir, 'result_manga.jpg'))