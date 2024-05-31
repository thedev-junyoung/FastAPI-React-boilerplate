#이 파일은 SQLAlchemy 세션을 설정하고 관리합니다. 데이터베이스와의 연결을 유지하고, 쿼리 실행 및 트랜잭션을 처리합니다.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from app.db.base import Base  # Base 클래스는 base_class.py에서 정의됩니다.
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL)

# 세션 로컬 클래스 구성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 세션을 얻는 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    데이터베이스 테이블을 생성합니다.
    """
    Base.metadata.create_all(bind=engine)