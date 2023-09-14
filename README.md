# 온프레미스 이커머스 환경에서 클라우드 기반의 라이브 커머스 플랫폼 구축
## 팀명 : 1번가
## My Role
### CI/CD
![image](https://github.com/KimDongHyun0907/1st-livecommerce-project/assets/88826811/5f5d6fda-113c-41a2-afcb-747aff6dd2ab)

• Gitlab, Jenkins, Terraform, k8s, AWS(EKS, Fargate)

• Gitlab과 Jenkins를 사용하여 EKS 클러스터와 EKS Fargate를 구축을 자동화한다.

• Gitlab repository에 EKS를 생성하는 terraform 코드를 push하면 Jenkins에서 자동으로 build되도록 한다.

• Gitlab에서 Jenkins 서버와 연결하는 webhook을 생성하면 push event를 발생 시 Jenkins에서 Gitlab에 Jenkinsfile을 통해 terraform 코드가 실행된다.

• 또한 Gitlab에 파일들을 push하는 과정을 자동화하기 위해 Python script를 작성한다.

• Python을 실행하면 terraform 파일들이 Gitlab에 push하여 EKS를 생성하는 과정을 자동화한다. 

### 챗봇 서비스 및 장바구니 사이트
![image](https://github.com/KimDongHyun0907/1st-livecommerce-project/assets/88826811/050b5561-ec7e-4a86-b532-8110f736e6d5)

• AWS (Lex, DynamoDB, Lambda, CloudWatch, EKS, Fargate, ALB, Route53), Python3, Flask, HTML, CSS, Javascript, Docker

• AWS Lex를 사용했고, 고객이 요구한 내용을 DynamoDB에 저장된 데이터를 불러와 AWS Lambda에서 처리한 후 Lex에서 메시지를 출력한다. 또한 요구한 내용을 전송하면 이벤트가 발생하므로 CloudWatch에서 로그를 확인할 수 있다.

• 기능은 구매목록 확인, 특정 서비스 정보 출력, 상품 추천이 있다.

• 장바구니 사이트에 구매할 상품들을 구매하면 구매한 정보가 DynamoDB에 저장된다.

• 챗봇, 장바구니 웹 서비스는 HTML/CSS, Javascript로 Front-End를 구현했고, AWS Lex와 DynamoDB를 불러오기 위해 Python Flask로 Back-End를 구현했다.

• 서버리스 아키텍처를 구현하기 위해 웹 파일을 Docker 이미지로 만들어 EKS Fargate를 사용했다.

• CI/CD로 구현한 EKS Cluster와 Fargate 프로필을 생성하고 ALB 인그레스 컨트롤러를 배포한 후 Route53으로 도메인을 설정했다.

### ARS 서비스
![image](https://github.com/KimDongHyun0907/1st-livecommerce-project/assets/88826811/a687edae-60db-47ed-aaee-5a3f76b40b9c)

• AWS (Connect, Lambda, DynamoDB, CloudWatch)

• AWS Connect를 사용했고, 고객이 요구한 내용을 DynamoDB에 저장된 데이터를 불러와 AWS Lambda에서 처리한 후 Connect에서 음성으로 출력한다.

• 기능은 고객이 상품을 주문하여 주문 정보를 확인한다는 가정하에 주문 목록 확인, 배송 상태 확인, 상담사 연결이 있다.

• 서비스를 사용하기 위해 회원인지 확인을 한다. 본인 확인을 위해 번호를 입력하고 회원 DB에 저장된 번호인지 확인을 한 후 서비스를 이용하게 한다.

• 또한 상담사 연결은 주중 오전 9시 ~ 오후 5시까지 설정하도록 하여 정해진 시간에만 연결을 할 수 있도록 구현했다
