import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

class Settings:
    """
    애플리케이션 설정을 관리하는 클래스
    """
    # 데이터베이스 연결 URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost/test_db")
    
    # 애플리케이션의 비밀 키 (JWT, OAuth 등에 사용)
    #SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    
    # CORS 허용할 오리진 목록
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "*").split(",")

    # 기타 설정
    #DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

# 설정 객체 생성
settings = Settings()
