## constaurant 프로젝트 구조

#### 바깥쪽 Constaurant 
: 'Project Root'   
django 프로젝트의 모든 파일이 담겨 있는 최상위 디렉토리   
이름을 마음대로 바꿔도 됨   

####  안쪽 Constaurant 
: 'Project App'   
우리 Project의 가장 중심이 되는 App   
이름을 바꾸면 많은 수정을 해야 함   

#### 'manage.py'
Django 프로젝트 관리를 위한 명령어를 지원   
앱(App) 생성, 데이터베이스 관련 명령, 개발서버 실행 등   

#### 'db.sqlite3'
우리 프로젝트에서 사용하는 데이터베이스 파일   

#### '__init__.py' 
Python 3.3 버전 이상부터는 이 파일이 없어도 python 패키지로 인식   
하위 버전 호환   

####  'settings.py'
시간대 설정, 데이터베이스 설정, 여러 경로 설정 등   
Django 프로젝트의 전반적인 설정을 담당

#### 'urls.py'
URL을 보고 알맞은 페이지로 연결해주는 역할   
ex) 소개 요청 url -> 소개 페이지   
ex) 로그인 요청 url -> 로그인 페이지   

#### 'wsgi.py'
WebServer Gateway Interface, WSGI   
웹 서버와 Python 어플리케이션인 Django가 소통하는데 필요한 일종의 프로토콜   

## foods 앱 구조
#### admin.py
앱을 django 관리자와 연동하기 위해 필요한 설정 파일

#### apps.py
앱에 대한 설정을 넣어두는 파일

#### models.py
django app에서 사용할 데이터 모델 정의   
데이터베이스 연동과 관련된 파일

#### views.py
django app의 메인 로직 처리와 관련된 파일

> djano 핵심 : models.py & views.py

#### tests.py
프로젝트의 테스트 코드를 작성하는 코드

#### migrations
데이터베이스의 변경 사항 히스토리 누적