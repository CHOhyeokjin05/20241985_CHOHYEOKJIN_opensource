from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import tempfile
import os
from PIL import Image
from total import translate_image

# FastAPI directory
# uvicorn main:app --reload

api_key = ""

# FastAPI 앱 초기화
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-image/")
async def process_image_endpoint(file: UploadFile = File(...)):
    # 업로드된 이미지를 PIL.Image로 로드
    input_image = Image.open(file.file)
    
    # 임시 파일을 생성하고 그 경로를 translate_image에 전달
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
        # 이미지를 임시 파일로 저장
        input_image.save(tmp_file, format="PNG")
        tmp_file_path = tmp_file.name  # 임시 파일 경로
        
        # 처리 함수 호출 (임시 파일 경로를 전달)
        output_image_path = translate_image(tmp_file_path, api_key)  # 이 값은 경로일 가능성 있음
        
        # output_image_path가 경로라면 그 경로를 사용해 이미지를 연다.
        output_image = Image.open(output_image_path)  # 경로로 이미지를 다시 열기
        
        # 처리된 이미지를 바이트로 변환하여 반환
        output_buffer = BytesIO()
        output_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)
        
        # 임시 파일 삭제
        os.remove(tmp_file_path)
        os.remove(output_image_path)  # 처리된 이미지도 삭제할 수 있음
    
    # 이미지 반환
    return StreamingResponse(output_buffer, media_type="image/png")
