# lecture_aws_for_ai
# data enginner
- 데이터 엔지니어는 데이터를 분석하기 위해 데이터를 수집, 저장, 가공하는 인프라를 구축하고 관리하는 업무를 합니다. 데이터 엔지니어링은 대량의 데이터를 관리하고 분석할 수 있도록 변환하는 기술을 의미합니다. 
## data enginner with aws
1. 서버리스로 구현 
- lambda, step fuction, glue
2. 데이터 수집을 할 때, 배치 프로세스로 구현(=일정한 주기로 실행하는 프로세스)
- api로 데이터 수집 
- eventbridge 
3. 데이터 가공 
- spark를 이용해서 대용량 데이터 가공 -> glue 
4. 가공된 데이터 저장 
- s3: raw 데이터 저장 & 이미지/음성 등 비정형 데이터 저장
- rdb: 가공된 & 관계성이 있는 정형 데이터 저장  


# data scientist 
- 데이터 사이언티스트(Data Scientist)는 데이터를 수집하고 분석하여 비즈니스 문제를 해결하고 의사결정을 내리는 전문가입니다. 데이터 과학자라고도 불리며, 데이터를 활용해 기업의 경쟁력을 높이는 역할을 합니다. 
## data scientist with aws
1. 가공된 데이터를 이용하여 데이터 전처리 
- ec2 & ecs
2. 전처리 데이터를 이용하여 모델 학습 
3. 학습된 모델을 서비스에 적용 


# web developer 
- 웹 개발자는 HTTP 프로토콜을 커뮤니케이션 매체로 사용하는 웹 페이지, 웹 사이트 등 WWW 기반 소프트웨어 개발자 또는 소프트웨어 엔지니어를 말한다.
## web developer with aws 
1. 학습된 모델을 이용해서 화면 구현 
2. rdb에 있는 데이터를 이용해서 화면 구현 

# devops
- DevOps(데브옵스)는 개발(Development)과 운영(Operation)을 통합하여 애플리케이션을 개발하고 운영하는 방법론입니다. 개발과 운영의 경계를 허물어 협업을 촉진하고, 자동화를 통해 효율성을 높이는 것을 목표로 합니다. 
## CI/CD 구축 
- codepipline & codebuild & cloudformation 

# 알람
## SNS 
- slack, cloudwatch, aws sns


