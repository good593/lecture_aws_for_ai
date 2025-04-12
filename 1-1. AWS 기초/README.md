---
style: |
  img {
    display: block;
    float: none;
    margin-left: auto;
    margin-right: auto;
  }
marp: true
paginate: true
---
# [서버-클라이언트 아키텍쳐](https://www.theknowledgeacademy.com/blog/client-server-architecture/)
- 기업(서버)이 고객(클라이언트)에게 서비스를 제공하는 아키텍처를 말합니다.

![w:900](./img/image.png)

---
- 고객이 증가하게 된다면, 기업은 더 많은 서버를 구매해야 합니다.

![w:900](./img/image-1.png)

---
- 갑자기 고객이 감소하게 된다면, 기업은 필요하지 않은 서버를 유지해야하는 어려움이 생깁니다.

![w:900](./img/image-2.png)

---
# [AWS(클라우드컴퓨팅)](https://aws.amazon.com/ko/what-is-cloud-computing/)
- AWS은 인터넷을 통해 원격으로 서버(가상 컴퓨터)를 **온디멘드**로 제공하고 사용한 만큼만 비용을 지불하는 서비스입니다.
  - **온디멘드(On Demand)**: 주문형 서비스
- 따라서 AWS은 기존 서버-클라이언트 아키텍쳐에 대한 문제점을 해결할 수 있습니다.
  - 고객이 증가하면, 서버를 더 많이 빌린다.
  - 고객이 감소하면, 빌린 서버를 줄인다.

---
![alt text](./img/image-3.png)

---
![alt text](./img/image-4.png)

---
# [AWS비용](https://aws.amazon.com/ko/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)
- AWS 요금은 수도세나 전기세와 같은 공과금을 납부하는 방식과 비슷합니다.
- 사용한 서비스에 대한 요금만 지불하고 사용을 중단하더라도 추가 비용이나 종료 비용이 없습니다.
- AWS 기본 트랙픽 요금 정책
  - AWS에서 인터넷으로 데이터 전달은 월 100GB 무료(EC2, S3, ELB 등)
  - 인터넷에서 AWS로 들어오는 트래픽은 언제나 무료

---
## AWS비용 확인 

![alt text](./img/image-5.png)

---
## [AWS비용 > 프리티어](https://aws.amazon.com/ko/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)

![alt text](./img/image-9.png)

---
### 언제나 무료
언제나 월별 일정 사용량은 무료
- 예) AWS Lambda 월 100만 요청 무료
- 예) Amazon CloudFront 월 1TB 트래픽 무료, HTTP/HTTPS 천만건,
CloudFront 함수 200만건 무료
- 예) Amazon DynamoDB(NoSQL DB) 월 25GB 저장공간, 월별 2억개 처리
용량 무료

---
### 12개월 무료
AWS 계정 생성 후 12개월동안만 적용되는 혜택
- 예) Amazon EC2 t3/t2.micro 월 750시간 무료
- 예) Amazon RDS t2/t3/t4g.micro 월 750시간 무료

### 무료 평가판
사용을 시작한 후 일정 기간 혹은 일정 사용량 사용 이후부터 요금 청구
- 예) Amazon QuickSight(AWS BI 시각화 툴): 처음 30일 무료
- 예) Amazon Chime(AWS의 커뮤니케이션 툴): 처음 30일 동안 PRO 티어 무료

---
## [AWS 글로벌 인프라](https://aws.amazon.com/ko/about-aws/global-infrastructure/?p=ngi&loc=0)

---
### Region(리전)
- AWS가 전 세계에서 데이터 센터를 클러스터링하는 물리적 위치를 리전이라고 합니다.
- 리전에는 여러 개의 가용영역이 있습니다.

---
- AWS는 리전을 통해 전세계에 서비스를 제공하고 있습니다.

![w:900](./img/image-6.png)

---
### Availability Zone(가용영역)
- 가용영역은 하나 이상의 개별 데이터 센터로 구성됩니다.
- 여러 가용영역에 걸쳐 서비스를 적용하면, 정전, 낙뢰, 지진 등과 같은 문제로 부터 안전하
게 보호됩니다

---
- 여러 가용영역에 걸쳐서 서비스를 제공할 수 있습니다.

![w:900](./img/image-7.png)

---
- AWS는 물리적인 가용영역을 각 가용영역 이름에 무작위로 매핑합니다.

![w:900](./img/image-8.png)


