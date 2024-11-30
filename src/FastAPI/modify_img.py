from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def process_image_with_text_overlay(image_path, data, translated_texts):
    """
    텍스트가 상자를 초과하면 블러 처리된 영역에 번호를 추가하고, 이미지 맨 아래에 흰색 영역과 텍스트를 추가합니다.

    Parameters:
        image_path (str): 원본 이미지 파일 경로
        data (list): 텍스트 감지 결과를 포함하는 리스트
        translated_texts (list): 번역된 텍스트 리스트

    Returns:
        img (Image.Image): 처리된 Pillow 이미지 객체
    """
    # 현재 파일 기준 경로 설정
    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, "ppocr_img/fonts/korean.ttf")

    # 이미지 로드
    img = Image.open(image_path).convert("RGBA")

    try:
        font = ImageFont.truetype(font_path, size=20)
    except Exception as e:
        raise FileNotFoundError(f"Error: Could not load font from path: {font_path}. {e}")

    draw = ImageDraw.Draw(img)
    extra_texts = []  # 이미지 하단에 출력할 텍스트 저장 리스트
    counter = 1  # 번호 카운터

    for index, item in enumerate(data):
        box_points = item[0]
        original_text = item[1][0]
        translated_text = translated_texts[index]

        # 경계 상자 좌표 계산
        x_min = int(min(p[0] for p in box_points))
        y_min = int(min(p[1] for p in box_points))
        x_max = int(max(p[0] for p in box_points))
        y_max = int(max(p[1] for p in box_points))

        # 박스 영역 블러 처리
        box_area = img.crop((x_min, y_min, x_max, y_max))
        blurred_area = box_area.filter(ImageFilter.GaussianBlur(15))
        img.paste(blurred_area, (x_min, y_min, x_max, y_max))

        # 텍스트 크기 계산
        text_bbox = draw.textbbox((0, 0), translated_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        box_width = x_max - x_min
        
        # # out of bound case 디버깅
        # text_width += 10000
        
        if text_width > box_width:  # 텍스트가 박스를 초과하는 경우
            # 블러 처리된 영역 위에 번호 추가
            number_text = str(counter)
            number_bbox = draw.textbbox((0, 0), number_text, font=font)
            text_x = x_min + (box_width - (number_bbox[2] - number_bbox[0])) / 2
            text_y = y_min + (y_max - y_min - (number_bbox[3] - number_bbox[1])) / 2
            draw.text((text_x, text_y), number_text, font=font, fill="white")
            
            # 하단 출력용 텍스트 저장
            extra_texts.append(f"{counter}. {original_text} → {translated_text}")
            counter += 1
        else:  # 텍스트가 박스 안에 들어가는 경우
            # 폰트 크기를 키워서 텍스트를 추가
            larger_font = ImageFont.truetype(font_path, size=30)  # 폰트 크기 키우기
            text_bbox = draw.textbbox((0, 0), translated_text, font=larger_font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            # 블러 처리된 박스 위에 텍스트 추가 (검은색으로)
            text_x = x_min + (box_width - text_width) / 2  # 텍스트 중앙 정렬
            text_y = y_min + (y_max - y_min - text_height) / 2  # 텍스트 수직 중앙 정렬
            draw.text((text_x, text_y), translated_text, font=larger_font, fill="black")  # 텍스트 색은 검은색

    # 이미지 아래에 흰색 영역 추가
    if extra_texts:
        extra_height = 30 * len(extra_texts) + 20  # 줄당 30px + 여백
        new_img = Image.new("RGBA", (img.width, img.height + extra_height), (255, 255, 255, 255))
        new_img.paste(img, (0, 0))
        img = new_img
        draw = ImageDraw.Draw(img)

        # 흰색 영역에 텍스트 추가
        y_text = img.height - extra_height + 10  # 여백 포함
        for line in extra_texts:
            draw.text((10, y_text), line, font=font, fill="black")
            y_text += 30  # 한 줄 간격

    return img
