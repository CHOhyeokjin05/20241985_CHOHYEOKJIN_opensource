# Ubuntu 20.04를 베이스 이미지로 사용
FROM ubuntu:20.04

# 환경 변수를 설정 (예: 타임존 설정)
ENV DEBIAN_FRONTEND=noninteractive

# 필요한 패키지들을 설치
RUN apt-get update && \
    apt-get install -y \
    python3.9 \
    python3.9-dev \
    python3-pip \
    python3.9-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libjpeg8-dev \
    zlib1g-dev \
    libblas-dev \
    liblapack-dev \
    git \
    curl \
    libxcb-xinerama0 \
    libx11-xcb1 \
    && apt-get clean

# pip 최신 버전으로 업데이트
RUN python3.9 -m pip install --upgrade pip

# 필요 패키지들 설치
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

# 컨테이너가 실행될 때 기본 명령어 설정
CMD ["python3.9"]

