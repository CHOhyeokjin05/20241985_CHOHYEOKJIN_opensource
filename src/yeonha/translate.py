# tkinter로 파일 선택해서 텍스트추출+번역

# pip install paddleocr openai pillow paddlepaddle


from paddleocr import PaddleOCR, draw_ocr
import openai
import os
from PIL import Image
from tkinter import Tk, filedialog
from typing import Optional, List, Tuple

class ImageTranslator:
    def __init__(self, api_key: Optional[str] = None):
        """
        이미지 번역기 초기화
        api_key: OpenAI API 키. 없으면 환경 변수에서 가져옴
        """
        # OpenAI API 키 설정
        if api_key:
            openai.api_key = api_key
        else:
            openai.api_key = os.getenv('OPENAI_API_KEY')
        
        if not openai.api_key:
            raise ValueError("OpenAI API 키가 필요합니다.")
        
        # PaddleOCR 초기화
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        
        # 현재 스크립트 경로
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        
    def extract_text_from_image(self, img_path: str) -> List[Tuple[List, Tuple[str, float]]]:
        """
        이미지에서 텍스트 추출
        """
        result = self.ocr.ocr(img_path, cls=True)
        return result[0] if result else []
        
    def translate_to_korean(self, text: str) -> str:
        """
        텍스트를 한국어로 번역
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful translator. Translate the following text to Korean."},
                    {"role": "user", "content": text}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"번역 중 오류가 발생했습니다: {str(e)}"
    
    def save_result_image(self, img_path: str, ocr_result: List, translated_texts: List[str]) -> str:
        """
        번역 결과를 이미지로 저장
        """
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in ocr_result]
        
        # 원본 텍스트와 번역된 텍스트를 합쳐서 표시
        combined_texts = [f"{line[1][0]} → {trans}" for line, trans in zip(ocr_result, translated_texts)]
        
        scores = [line[1][1] for line in ocr_result]
        
        font_path = os.path.join(self.script_dir, 'ppocr_img/fonts/simfang.ttf')
        result_image = draw_ocr(image, boxes, combined_texts, scores, font_path=font_path)
        result_image = Image.fromarray(result_image)
        
        output_path = os.path.join(self.script_dir, 'result_translated.jpg')
        result_image.save(output_path)
        return output_path

def select_file() -> str:
    """
    파일 탐색기를 열어 사용자가 이미지를 선택하도록 함
    """
    root = Tk()
    root.withdraw()  # GUI 창을 숨김
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("All Files", "*.*")
        ]
    )
    root.destroy()  # Tkinter 루트를 종료
    if not file_path:
        raise ValueError("이미지 파일이 선택되지 않았습니다.")
    return file_path

def main():
    # API 키 설정 (실제 사용시에는 환경 변수나 설정 파일에서 가져오는 것을 권장)
    api_key = ""
    
    # 이미지 번역기 초기화
    translator = ImageTranslator(api_key)
    
    try:
        # 파일 탐색기를 통해 이미지 파일 선택
        img_path = select_file()
    except ValueError as e:
        print(str(e))
        return
    
    # 이미지에서 텍스트 추출
    ocr_result = translator.extract_text_from_image(img_path)
    
    print("=== 번역 결과 ===")
    translated_texts = []
    
    # 각 텍스트 라인에 대해 번역 수행
    for line in ocr_result:
        original_text = line[1][0]  # OCR로 인식된 텍스트
        translated = translator.translate_to_korean(original_text)
        translated_texts.append(translated)
        
        print(f"\n원문: {original_text}")
        print(f"번역: {translated}")
    
    # 번역 결과가 포함된 이미지 저장
    output_path = translator.save_result_image(img_path, ocr_result, translated_texts)
    print(f"\n번역 결과 이미지가 저장되었습니다: {output_path}")

if __name__ == "__main__":
    main()
