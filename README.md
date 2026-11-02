# 📚 스터디 출석 관리 프로그램

파이썬 표준 라이브러리만으로 구현한 CLI 기반 스터디 출석부 프로그램입니다.  
Docker 컨테이너로도 실행할 수 있습니다.

## 🔧 요구사항

- Python 3.9 이상
- (선택) Docker 20.10 이상
- Git

## 📂 프로젝트 구조

```
study-attendance/
├── attend.py           # 메인 프로그램
├── attendance.json     # 출석 데이터(샘플 포함)
├── Dockerfile          # Docker 이미지 빌드 설정
├── requirements.txt
└── README.md
```

## 🚀 로컬 실행

```bash
# 1) 저장소 복제
git clone https://github.com/<your-id>/study-attendance.git
cd study-attendance

# 2) 실행 권한 부여
chmod +x attend.py

# 3) 실행
python attend.py
```

## 🐳 Docker 실행

### 사전 확인

```bash
docker --version
# Docker version 24.0.6, build ed223bc

docker run hello-world
# Hello from Docker! ... (정상 출력 확인)
```

### 이미지 빌드 & 실행

```bash
# 이미지 빌드
docker build -t study-attendance:1.0 .

# 빌드된 이미지 확인
docker images | grep study-attendance

# 컨테이너 실행 (-it: 대화형, --rm: 종료 시 삭제, -v: 데이터 영속화)
docker run -it --rm \
  -v $(pwd)/attendance.json:/app/attendance.json \
  study-attendance:1.0

# 실행 중 컨테이너 확인
docker ps
```

## 🔗 Git 원격 저장소 연동

```bash
git init
git add .
git commit -m "feat: 스터디 출석부 초기 구현"
git branch -M main
git remote add origin https://github.com/<your-id>/study-attendance.git
git push -u origin main
```

## 🧪 기능

| 번호 | 기능 | 설명 |
|-----|------|------|
| 1 | 출석 체크 | 날짜/이름 입력(날짜 생략 시 오늘), 중복 방지 |
| 2 | 출석 목록 보기 | 날짜순 정렬 출력 |
| 3 | 종료 | 시스템 종료 |