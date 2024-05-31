import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import router as api_v1_router
from app.db.session import create_tables  # 올바르게 임포트
from app.core.config import settings

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,  # 실제 운영 환경에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 테이블 생성
create_tables()

# API 라우터 포함
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}



# === build 패키징 ===================================================== //위의 '/' 엔드포인트 삭제 해야함. 
""" from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

# React 빌드 디렉토리 경로
build_path = Path(__file__).parent.parent.parent / "frontend" / "build"

# 모든 경로를 처리하는 엔드포인트
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_react_app(full_path: str):
    return (build_path / "index.html").read_text()


# 정적 파일 제공
app.mount("/static", StaticFiles(directory=build_path / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_react_app():
    return (build_path / "index.html").read_text() """


""" 
작동 방식
정적 파일 서빙: 
app.mount("/static", StaticFiles(directory=build_path / "static"), name="static")은 
React 애플리케이션의 정적 파일을 /static 경로에서 제공하도록 설정합니다.

루트 경로 처리: 
@app.get("/", response_class=HTMLResponse)는 '/' 경로로 들어오는 요청에 대해 
React 애플리케이션의 index.html을 반환합니다.

모든 경로 처리: 
@app.get("/{full_path:path}", response_class=HTMLResponse)는 
/api/v1가 아닌 모든 경로로 들어오는 요청에 대해 React 애플리케이션의 index.html을 반환합니다. 
여기서 full_path는 경로 변수로서 모든 경로를 캡처합니다. 
이는 클라이언트 사이드 라우팅을 위해 모든 경로를 index.html로 리디렉션하여 React 라우터가 해당 경로를 처리할 수 있게 합니다.
"""