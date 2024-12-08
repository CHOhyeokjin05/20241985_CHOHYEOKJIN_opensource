# 만화 번역 프로그램

**분반:** 1팀  
**학번:** 20241985  
**이름:** 조혁진  

---

## 설명

만화나 '짤'의 번역에 있어 기존 방법은 비효율적이었다. 사이트에서 번역된 작업물을 찾거나 구글 이미지 번역, 빅스비 비전을 사용했지만, 문어체나 부적절한 존댓말이 사용되거나 번역된 텍스트가 그림을 가리는 문제가 있었다. 이를 해결하기 위해 이미지 캡셔닝 신경망을 사용해 상황에 맞는 설명을 생성하고, 이를 ChatGPT와 같은 LLM에 넣어 자연스럽고 정확한 번역을 시도했다. 또한, 번역된 텍스트가 그림을 가리면 번호를 넣고 공간을 만들어 문제를 해결했다. FastAPI를 사용해 API로 제작했지만, 버전 1에서는 수직 일본어를 인식하지 못하는 문제를 겪었다. Manga-OCR을 적용했으나 텍스트가 강조된 이미지에서만 잘 작동했고, 이를 해결하기 위해 Poricom 오픈소스를 발견해 수정 후 버전 2 프로그램을 제작했다.

<hr/>

## 구현 방법

> ___글자 추출___: PaddleOCR, Manga-OCR, tesserocr 이용

> ___번역___: 추출된 텍스트 + image captioning(Hugging Face ViT)상황 설명 텍스트 -> ChatGPT API

> ___이미지 수정___: Pillow 이용

> ___API___: FastAPI 이용

> ___오픈 소스___: Poricom 이용

<hr/>

## 출처
## 참고 자료 목록

1. [PaddleOCR - GitHub](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README_en.md)  
   Open-source OCR tool designed for a variety of text recognition tasks.

2. [Manga-OCR - GitHub](https://github.com/kha-white/manga-ocr)  
   Specialized OCR for recognizing Japanese text in manga images.

3. [ImageCaptioning - TensorFlow](https://www.tensorflow.org/text/tutorials/image_captioning)  
   A tutorial on implementing image captioning using TensorFlow.

4. [vit-gpt2-image-captioning - Hugging Face](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)  
   Image captioning model combining Vision Transformer (ViT) and GPT-2.

5. [The Illustrated Image Captioning Using Transformers - Blog](https://ankur3107.github.io/blogs/the-illustrated-image-captioning-using-transformers/)  
   A detailed explanation of image captioning using transformer models.

6. [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)  
   Official documentation for using OpenAI's API services.

7. [Pillow 이미지에 텍스트 추가하기 - Tistory](https://daco2020.tistory.com/832)  
   A tutorial on adding text to images using the Python Pillow library.

8. [OpenCV를 사용한 이미지 처리 – 블러링 - Tistory](https://data-science-note.tistory.com/33)  
   Guide on using OpenCV for image processing, focusing on blurring techniques.

9. [FastAPI 이미지 업로드, 다운로드 구현하기 - Tistory](https://mopil.tistory.com/m/63)  
   Implementation guide for image upload and download features using FastAPI.

10. [Poricom - GitHub](https://github.com/blueaxis/Poricom)  
    Open-source manga translation tool built with PyQt.

11. [Probing the Need for Visual Context in Multimodal Machine Translation - arXiv](https://arxiv.org/abs/1903.08678)  
    Research paper on the significance of visual context in multimodal translation systems.


---

## 참고
ubuntu_20.04_20241985_build.yaml은 버전 1 프로그램 콘다 환경 만들 수 있는 yaml 파일입니다.
버전 2 프로그램 콘다 환경은 Upgrade_Poricom-main 디렉토리에 build 디렉토리에 있습니다.
