# 만화 번역 프로그램

**분반:** 1팀  
**학번:** 20241985  
**이름:** 조혁진  

---

## 설명

많은 만화와 이미지가 일본어나 영어로 되어 있어 번역이 필요하지만, 기존 번역 프로그램들은 텍스트에 그림이 가려지고 자연스러운 구어체 번역을 제공하지 못한다. 따라서 번역된 텍스트가 그림을 가리지 않도록 번호를 붙여 만화 밑에 표시하는 방법과, 이미지 설명 생성(image captioning)과 ChatGPT API를 활용한 번역을 적용하는 방법으로 문제를 해결한다. 이 프로그램은 Python으로 구현되며, Android에서 사용할 수 있도록 FastAPI를 통해 API로도 제공할 계획이다.

<hr/>

## 구현 방법

> ___글자 추출___: Google Visioin or PaddleOCR 이용

> ___번역___: 추출된 텍스트 + image captioning(TensorFlow)상황 설명 텍스트 -> ChatGPT API

> ___이미지 수정___: OpenCV or pillow 이용

> ___API___: FastAPI 이용

<hr/>

## 출처
1. [PaddleOCR, github](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README_en.md)
2. [OCR 최신 동향, 2022_02_08, github pages](https://yongwookha.github.io/MachineLearning/2022-02-08-current-ocrs)
3. [MRN for Incremental Multilingual Text Recognition, github](https://github.com/simplify23/MRN/blob/main/README.md)
4. [OpenAI API reference, OpenAI Platform](https://platform.openai.com/docs/api-reference/introduction)
5. [pillow 이미지에 텍스트 추가하기, tistory](https://daco2020.tistory.com/832)
6. [OpenCV 이미지 테두리 만들기, VirusHeo](https://virusheo.blogspot.com/2022/05/220528.html)
7. [점프 투 FastAPI, 박응용](https://wikidocs.net/book/8531)

