from sqlalchemy import Column, Integer, String, Boolean  # SQLAlchemy의 Column, Integer, String, Boolean 클래스를 가져옵니다.
from sqlalchemy.orm import relationship  # 관계 설정을 위해 relationship을 가져옵니다.
from app.db.base_class import Base  # 모든 모델이 상속받는 기본 클래스인 Base를 가져옵니다.

# User 클래스는 SQLAlchemy의 Base 클래스를 상속받아 데이터베이스 모델을 정의합니다.
class User(Base):
    __tablename__ = "users"  # 데이터베이스 테이블 이름을 지정합니다.

    # 데이터베이스 컬럼을 정의합니다.
    id = Column(Integer, primary_key=True, index=True)  # id 컬럼: 기본 키, 인덱스 생성
    email = Column(String(255), unique=True, index=True)  # email 컬럼: 고유 값, 인덱스 생성, 최대 길이 255
    username = Column(String(255), unique=True, index=True)  # username 컬럼: 고유 값, 인덱스 생성, 최대 길이 255
    hashed_password = Column(String(255))  # hashed_password 컬럼: 최대 길이 255
    is_active = Column(Boolean, default=True)  # is_active 컬럼: 기본 값은 True

    # relationship()은 다른 테이블과의 관계를 설정할 때 사용됩니다.
    # 예를 들어, 사용자가 작성한 게시물을 정의할 때 사용할 수 있습니다.
    # posts = relationship("Post", back_populates="owner")  # 예시: User와 Post 모델 간의 관계 정의

""" 
이 User 클래스는 SQLAlchemy ORM을 사용하여 데이터베이스의 "users" 테이블과 매핑되는 Python 클래스를 정의합니다. 
이 클래스는 사용자의 ID, 이메일, 사용자명, 해시된 비밀번호, 활성화 상태 등의 정보를 저장합니다. 
또한, SQLAlchemy의 Column 클래스를 사용하여 각 속성의 데이터 타입과 제약 조건을 지정합니다.
"""