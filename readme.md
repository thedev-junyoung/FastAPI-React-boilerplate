# React + FastAPI Boilerplate

## 폴더 구조
```bash
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── v1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dependencies
│   │   │   │   ├── endpoints
│   │   │   │   │   └── user.py
│   │   │   │   ├── routers.py
│   │   │   │   └── utils
│   │   │   │       └── pagination.py
│   │   │   └── v2
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── crud
│   │   │   └── user.py
│   │   ├── db
│   │   │   ├── base.py
│   │   │   ├── base_class.py
│   │   │   └── session.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── post.py
│   │   │   └── user.py
│   │   └── schemas
│   │       └── user.py
│   ├── docker-compose.yml
│   ├── mysql-init
│   │   └── init.sql
│   └── requirements.txt
└── frontend
    ├── README.md
    ├── package-lock.json
    ├── package.json
    ├── public
    │   ├── favicon.ico
    │   ├── index.html
    │   ├── logo192.png
    │   ├── logo512.png
    │   ├── manifest.json
    │   └── robots.txt
    └── src
        ├── App.css
        ├── App.js
        ├── App.test.js
        ├── components
        │   ├── PostForm.js
        │   ├── PostList.js
        │   ├── UserForm.js
        │   └── UserList.js
        ├── index.css
        ├── index.js
        ├── logo.svg
        ├── reportWebVitals.js
        └── setupTests.js
```

### 백엔드 구조
- `api/v1/endpoints/user.py`: 사용자 관련 CRUD 엔드포인트 정의
- `core/config.py`: 애플리케이션 설정 관리
- `core/security.py`: 보안 관련 설정 및 기능
- `crud/user.py`: 사용자 데이터베이스 CRUD 로직
- `db/session.py`: 데이터베이스 세션 설정
- `db/base.py`: 모든 모델을 등록하여 SQLAlchemy가 이를 인식하고 테이블을 생성할 수 있게 함
- `db/base_class.py`: 데이터베이스 모델의 베이스 클래스를 정의
- `main.py`: FastAPI 애플리케이션 진입점
- `models/user.py`: 사용자 데이터베이스 모델 정의
- `schemas/user.py`: 사용자 Pydantic 스키마 정의

### 프론트엔드 구조
- `src/App.js`: 메인 React 컴포넌트
- `src/components/UserForm.js`: 사용자 작성/수정 폼 컴포넌트
- `src/components/UserList.js`: 사용자 리스트 컴포넌트

### 설정 및 실행

#### 요구 사항
- Docker
- Docker Compose
- Node.js (v14 이상)
- Python (3.9 이상)

#### 백엔드 설정 및 실행

1. **백엔드 의존성 설치**
```bash
cd backend pip install -r requirements.txt
```
2. **Docker 컨테이너 실행**
```bash
docker-compose up --build
```
3. **FastAPI 서버 실행**
Docker Compose가 모든 서비스를 시작하면 FastAPI 서버가 `http://localhost:8000`에서 실행됩니다.
    

#### 프론트엔드 설정 및 실행

1. **프론트엔드 의존성 설치**
```bash
cd frontend npm install
```    
2. **React 애플리케이션 실행**
```bash
npm start
```
React 개발 서버가 `http://localhost:3000`에서 실행됩니다.

### 주요 기능
- **사용자 생성**: 사용자를 생성하는 API와 폼 제공
- **사용자 조회**: 전체 사용자 목록을 조회하는 API와 리스트 컴포넌트 제공
- **사용자 업데이트**: 사용자를 업데이트하는 API와 폼 제공
- **사용자 삭제**: 사용자를 삭제하는 API와 버튼 제공

### API 엔드포인트
- `GET /api/v1/users/`: 전체 사용자 목록 조회
- `POST /api/v1/users/`: 새 사용자 생성
- `GET /api/v1/users/{user_id}`: 특정 사용자 조회
- `PUT /api/v1/users/{user_id}`: 특정 사용자 업데이트
- `DELETE /api/v1/users/{user_id}`: 특정 사용자 삭제
### 주의 사항
- 환경 변수 설정은 `.env` 파일을 사용하여 관리합니다.
- 데이터베이스 초기화 스크립트는 `mysql-init/init.sql` 파일을 사용합니다.
- 개발 환경에서는 `DEBUG` 모드를 활성화하세요.