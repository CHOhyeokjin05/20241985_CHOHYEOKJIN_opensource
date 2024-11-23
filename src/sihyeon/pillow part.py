from PIL import Image, ImageDraw, ImageFont
import textwrap

def insert_translated_text(image_path, output_path, text_regions, font_path=None):
    """
    번역된 텍스트를 이미지에 삽입하는 함수.

    :param image_path: 원본 이미지 파일 경로.
    :param output_path: 결과 이미지를 저장할 경로.
    :param text_regions: 텍스트 영역 정보 리스트. 각 항목은 딕셔너리로 구성.
        - 'bbox': (left, top, right, bottom)의 좌표 튜플.
        - 'translated_text': 번역된 텍스트 문자열.
    :param font_path: 사용할 폰트 파일의 경로. 기본 폰트를 사용하려면 None으로 설정.
    """
    # 이미지 열기
    image = Image.open(image_path).convert('RGBA')
    draw = ImageDraw.Draw(image)

    # 기본 폰트 설정
    if font_path:
        font = ImageFont.truetype(font_path, size=20)
    else:
        font = ImageFont.load_default()

    for region in text_regions:
        bbox = region['bbox']
        translated_text = region['translated_text']

        # 텍스트 영역 지우기 (투명 처리)
        draw.rectangle(bbox, fill=(255, 255, 255, 0))

        # 텍스트 영역 크기에 맞게 텍스트 줄바꿈 처리
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        lines = textwrap.wrap(translated_text, width=15)  # 필요한 경우 width 조정

        # 텍스트 높이 계산
        line_height = font.getsize('A')[1]
        total_text_height = line_height * len(lines)

        # 텍스트 시작 위치 계산 (세로 중앙 정렬)
        y_text = bbox[1] + (text_height - total_text_height) / 2

        for line in lines:
            line_width = font.getsize(line)[0]
            x_text = bbox[0] + (text_width - line_width) / 2  # 가로 중앙 정렬

            # 텍스트 그리기 (검은색)
            draw.text((x_text, y_text), line, fill='black', font=font)
            y_text += line_height

    # 이미지 저장
    image.save(output_path)



#사용 방법(예시)
# 예제 데이터
image_path = 'original_comic_page.jpg'
output_path = 'translated_comic_page.jpg'
text_regions = [
    {
        'bbox': (50, 100, 200, 150),
        'translated_text': '안녕하세요, 반갑습니다!'
    },
    {
        'bbox': (300, 200, 450, 250),
        'translated_text': '이것은 번역된 텍스트입니다.'
    }
]

# 폰트 파일 경로 (옵션)
font_path = 'fonts/arial.ttf'  # 필요에 따라 경로 수정

# 함수 호출
insert_translated_text(image_path, output_path, text_regions, font_path)
