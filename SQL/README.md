# 데이터 분석을 위한 SQL 기초 공부
---
## 환경 설정

### 파이썬 패키지 관리자 - pip
pip는 파이썬 원격 모듈 저장소인 PyPI로부터 패키지를 가져와 내 컴퓨터로 설치할 수 있는 환경을 만들어주는 패키지 매니저이다.

- pip를 통해 패키지를 설치 하는 기본적인 방법

```bash
pip install <패키지명>
```
위 명령어를 통해 모듈 패키지를 원격 저장소인 PyPI로 부터 다운받아 설치할 수 있다.

### 패키지(모듈)간의 버전 충돌을 피하기 위해, 각 작업이나 프로젝트에 맞는 가상 환경을 생성해보기. - AnaConda
- 가상환경이 필요한 이유 -> 각 프로젝트마다 Required Dependancy(모듈의 버전)가 다를 수 있기 때문에 프로젝트별로 환경을 분리해서 활용하고 싶어서.

- Anaconda는 Conda프로젝트에 여러가지 같이 포함해둔 구조

Anaconda Environments 에서 가상환경을 생성해보기
1. Anaconda Navigator 실행
2. Anaconda Environments 탭으로 이동
3. 새로운 가상환경을 추가하고 싶다면, Create를 눌러 원하는 이름 생성
4. 가상환경을 세팅한 상태로 설치된 패키지를 보면, base(root)와 설치된 환경이 다른것을 볼 수 있음!
5. 이제 마음껏 설치하고 SQL공부 드가자~