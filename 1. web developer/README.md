# [uv](https://docs.astral.sh/uv/getting-started/)

## [Python 패키징이 복잡해진 역사](https://sigridjin.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%9D%BC%EB%A9%B4-uv-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%A9%EC%8B%9C%EB%8B%A4-546d523f7178)
- Python 생태계는 오랫동안 패키지 관리, 버전 관리, 가상환경 관리, 빌드 도구 등이 파편화되어 혼란스럽다는 평가를 받아왔습니다.
- Astral이 만든 `uv`는 2024년 초에 출시되어, `pip`, `poetry`, `conda` 등 다양한 도구들의 장점을 통합하고, Rust를 활용한 초고속 의존성 해석(Resolver)으로 큰 주목을 받고 있습니다.
- Anthropic, OpenAI 를 포함한 실제 ML/DS(데이터 사이언스), 백엔드, 오픈소스 프로젝트 등 여러 분야에서 `uv` 도입 사례가 급격히 늘고 있습니다.


## [install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
- window
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- macOS & Linux
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## [파이썬 설치 및 조회](https://docs.astral.sh/uv/guides/install-python/)
- 설치된 파이썬 조회 
```shell
uv python list
```
- 파이썬 설치 
```shell
uv python install 3.12
```

## [가상환경](https://docs.astral.sh/uv/getting-started/features/#the-pip-interface)
- 가상환경 생성 
```shell
uv venv .venv -p 3.12
```
- 가상환경 접속 
```shell
.venv\Scripts\activate
```
- 의존성 라이브러리 설치
```shell
uv pip install -r requirements.txt
```

# docker 
- build 
```shell
# Make docker image
docker build --platform linux/amd64 -t streamlit-image .
docker images # 생성된 이미지 확인 
```
- Run container 
```shell
# 윈도우
docker run --name streamlit-container -d -p 8501:8501 -e host=database-1.czs2guui4eo1.ap-northeast-2.rds.amazonaws.com streamlit-image
docker ps # 실행중인 컨테이너 확인 
```
- web 접속 
```shell
http://localhost:8501
```
