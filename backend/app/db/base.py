from app.db.base_class import Base
from app.models.user import User

# 여기에서 모든 모델을 임포트하여 Base에 등록합니다.
# Base.metadata.create_all(bind=engine) 호출 시 모든 테이블이 생성됩니다.
