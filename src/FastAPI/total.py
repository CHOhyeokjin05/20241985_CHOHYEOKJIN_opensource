from paddleocr import PaddleOCR
import openai
import os
from typing import Optional, List, Tuple
import modify_img

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
        
    def translate_to_korean(self, text: str, caption: str) -> str:
        """
        텍스트를 한국어로 번역
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[ 
                    {"role": "system", "content": f"You are a helpful translator.\nImage Description: {caption}\nTranslate the following text to Korean.\n"},
                    {"role": "user", "content": f'{text}'}
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
        # `process_image_with_text_overlay`를 사용하여 번역된 텍스트를 이미지에 오버레이합니다.
        image = modify_img.process_image_with_text_overlay(img_path, ocr_result, translated_texts)
        
        # 결과 이미지를 저장할 경로
        output_path = os.path.join(self.script_dir, "result_translated_with_blur.png")
        
        # 이미지 저장
        image.save(output_path)
        
        return output_path

def translate_image(img_path: str, caption: str, api_key: Optional[str] = None) -> str:
    """
    주어진 이미지 경로에 대해 텍스트를 추출하고 번역한 후, 번역된 텍스트로 이미지를 저장
    """
    # 이미지 번역기 초기화
    translator = ImageTranslator(api_key)
    
    # 이미지에서 텍스트 추출
    ocr_result = translator.extract_text_from_image(img_path)
    
    print("=== 번역 결과 ===")
    translated_texts = []
    
    # 각 텍스트 라인에 대해 번역 수행
    for line in ocr_result:
        original_text = line[1][0]  # OCR로 인식된 텍스트
        translated = translator.translate_to_korean(original_text, caption)
        translated_texts.append(translated)
        
        print(f"\n원문: {original_text}")
        print(f"번역: {translated}")
    
    # 번역 결과가 포함된 이미지 저장
    output_path = translator.save_result_image(img_path, ocr_result, translated_texts)
    print(f"\n번역 결과 이미지가 저장되었습니다: {output_path}")
    
    return output_path


# 사용 예시 (다른 파일에서 호출)
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(script_dir, "ppocr_img/imgs_en/img_12.jpg")  # 실제 이미지 경로 입력
    api_key = ""  # OpenAI API 키 설정
    caption = 'manga'
    
    translated_image_path = translate_image(img_path, caption, api_key)