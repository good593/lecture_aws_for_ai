# local PC
## docker 
- build 
```shell
# Make docker image
docker build --platform linux/amd64 -t streamlit-image .
docker images # 생성된 이미지 확인 
```
- Run container 
```shell
# 윈도우
docker run --name streamlit-container -d -p 8501:8501 streamlit-image

docker ps # 실행중인 컨테이너 확인 
```
- web 접속 
```shell
http://localhost:8501
```
