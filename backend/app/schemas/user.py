from pydantic import BaseModel

# 공통 속성을 정의하는 기본 클래스
class UserBase(BaseModel):
    username: str  # 사용자명: 문자열
    email: str  # 이메일: 문자열

# 사용자 생성을 위한 클래스, 비밀번호를 포함
class UserCreate(UserBase):
    password: str  # 비밀번호: 문자열

# 사용자 업데이트를 위한 클래스, 비밀번호를 포함
class UserUpdate(UserBase):
    password: str  # 비밀번호: 문자열

# 데이터베이스에 저장된 사용자 정보를 위한 기본 클래스
class UserInDBBase(UserBase):
    id: int  # 사용자 ID: 정수

    class Config:
        orm_mode = True  # ORM과 호환되도록 설정

# 클라이언트에 반환할 사용자 정보를 위한 클래스
class User(UserInDBBase):
    pass  # UserInDBBase를 그대로 상속받아 사용


""" 
Pydantic: 데이터 검증과 직렬화를 위해 사용하는 라이브러리입니다. FastAPI와 함께 사용되어 입력 데이터의 유효성을 검사하고 응답 데이터를 자동으로 직렬화합니다.
BaseModel: Pydantic의 기본 모델 클래스입니다. 모든 Pydantic 모델은 이 클래스를 상속받아야 합니다.
스키마: 데이터 모델을 정의하고, 데이터를 검증 및 직렬화하기 위한 청사진입니다. FastAPI에서는 요청 바디와 응답 데이터의 검증을 위해 사용됩니다.

Pydantic 모델은 DTO와 유사한 개념으로, 데이터 검증과 직렬화를 담당합니다. 
FastAPI에서는 Pydantic 모델을 사용하여 입력 데이터의 유효성을 검증하고, 응답 데이터를 구조화하여 클라이언트에 반환합니다. 
이를 통해 애플리케이션의 신뢰성과 보안성을 높일 수 있습니다.

"""