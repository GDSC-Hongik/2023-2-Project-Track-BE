###  다음 내용은 GDSC Hongik 2023-2-Project-Track-BE 에서 배운 내용을 정리한 글입니다. 

# **Web Server Gateway Interface(wsgi)**

프로젝트 앱 디렉토리에 있는 WSGI는 WebServer Gateway Interface의 약자로 파이썬에서 웹 통신을 하기 위한 일종의 약속이다. 이는 웹 서버와 웹 어플리케이션 서버(여기서는 장고)를 연결해주는 역할을 한다라고 설명이 되어있었다.

### 웹 서버(Web Server)와 웹 어플리케이션 서버(Web Application Server)는 무슨 차이가 있을까?

웹 서버는 HTTP를 통해 클라이언트에게 요청을 받고, 그 요청에 따라 HTML 문서를 제공한다. HTML 문서를 파싱하면서 각 태그에 따른 image, css, javascript와 같은 외부 리소스에 대한 추가적인 HTTP 요청을 한다. (HTML과 외부 리소스를 한번에 요청하지 않고 별도로 요청하는 이유는 병렬 다운로드로 웹 페이지 로딩 시간을 단축할 수 있다는 점과 캐싱의 이점을 살리기 위함이다. )

HTML과 정적 리소스(이미지, CSS, javascript)를 제공하는 소프트웨어를 웹 서버라고 부른다. 또한 동적인 콘텐츠 제공을 위한 요청을 웹 어플리케이션 서버에 보내주는 역할도 한다. 

웹 서버의 예시로는 Apache HTTP Server, Nginx, Microsoft Internet Information Services (IIS)가 있다. 

웹 어플리케이션 서버는 서버 측에서 실행되며 사용자의 요청에 따라 동적인 콘텐츠를 생성하고 데이터베이스와 상호작용하는 복잡한 작업을 수행하는 소프트웨어이다. 동적인 콘텐츠라함은 주로 복잡한 로직을 처리하고 데이터베이스의 CRUD 작업 처리등이 있다. 

웹 어플리케이션 서버의 예시로는 Django, Flask, Ruby on Rails 등이 있다. 

웹 서버는 주로 정적인 컨텐츠를 처리하는데 최적화되어있지만 웹 어플리케이션의 서버는 클라이언트의 요청을 처리하기 위한 동적 콘텐츠 생성에 초점을 맞추고 있다. 

WSGI Server (Middleware)

WSGI 서버는 클라이언트로부터 HTTP 요청을 받아 WSGI 인터페이스를 통해 파이썬 애플리케이션 서버에 전달합니다.

또한 파이썬 애플리케이션으로부터 받은 응답을 HTTP 응답으로 클라이언트에게 전달하는 역할을 합니다.

WSGI 애플리케이션서버

웹 요청을 받아 처리하고 응답을 생성하는 코드의 모음입니다. 

데이터베이스 상호작용이나 복잡한 작업을 수행합니다. 

Django Project를 배포할 때 사용했던 pythonanywhere 사이트에서 WSGI configure file을 변경해주었는데 나는 장고라는 웹 어플리케이션 서버를 사용했으니까 해당 포맷으로 맞춰달라는 의미를 전달해준 것이라 추측할 수 있다. 


# ****MVC 아키텍처와 MVT 아키텍처****

장고는 MVT아키텍처를 가지고있다. 

MVT는 Model View Template로 이루어진 아키택처 패턴인데, 이 구성요소를 하나씩 살펴보자. 

## Model

모델은 DB 구조를 정의하고 DB와의 상호작용을 캡슐화한다. Django는 ORM(Object-Relational Mapping)을 통해 데이터베이스 테이블에 대응되며 이를 통해 따로 SQL을 작성하지 않고 DB작업을 수행할 수 있다. 

각 class에 선언된 클래스변수는 테이블의 컬럼에 해당한다.

## View

view는 로직을 담당한다. HTTP로 넘겨진 요청에 따라 처리를 해주는 urls.py에서는 view의 함수를 호출한다. 그러면 view의 함수에서는 DB에 있는 data중 필요한 것들을 조회하기위해 model을 호출합니다. 그렇게 해서 얻은 데이터를 템플릿에 전달하여 동적인 웹 페이지를 생성해주고, 생성된 웹페이지나 기타 응답코드를 클라이언트에게 반환하는 역할을 합니다.

Django에서는 함수 기반 뷰(Function-Based Views, FBVs)와 클래스 기반 뷰(Class-Based Views, CBVs)의 두 가지 형태가 존재합니다. 사진에서는 함수 기반 뷰를 사용했습니다. 클래스 기반 뷰를 사용하면 재사용이 가능하고, 복잡한 웹 애플리케이션을 좀 더 체계적으로 관리할 수 있습니다.

## Template

웹 어플리케이션의 보여지는 부분을 담당한다. Template는 HTML을 기반으로 하지만 Django Template Language (DTL)이라는 자체 템플릿 시스템을 사용하여 동적 데이터를 HTML에 삽입할 수 있도록 확장된다. 이러한 동적 데이터를 보여주기 위해 템플릿 태그와 템플릿 변수를 활용한다. 이때 사용되는 템플릿 태그를 통해 코드를 재사용할 수 있다. (상속 class와 같이 )

현재 내가 진행하고있는 Flutter로 개발중인 프로젝트는 MVC 구조를 사용하고 있다. 사용자의 입력을 받아 내부 로직을 처리하고 모델을 이용해 데이터를 조작하고 뷰를 통해 결과를 표시하도록 하는 매개자 역할이 Controller인데, 이런 MVC(Model, View, Controller) 구조를 사용하게 되면 Django의 Template에서 하던 비지니스 로직을 View에서 처리한다. 그리고 Django의 View에서 진행하던 사용자의 인터페이스역할과 모델과의 상호작용, 템플릿 랜더링등의 결정을 MVC 구조에서는 컨트롤러가 한다. 

이처럼 View와 Controller가 따로 존재하므로 프론트앤드와 디자이너가 분업화하기 쉽다. 하지만 Django의 MVT는 웹 애플리케이션에 특화되어 있으며, 개발 속도와 효율성이 중요한 소규모 팀 또는 단일 개발자 프로젝트에 더 적합할 수 있다.

# **ORM**

$migration$

# **마이그레이션**

마이그레이션은 모델의 변경사항을 관리하는 방법이다.

장고에서 모델은 class로 정의되며 이 class는 Django ORM(Object-Relational Mapping)을 통해 Database table에 매핑된다. 따라서 우리 모델의 데이터필드 type이 변한다던가 모델의 데이터 필드가 한개 추가된다던가와 같은 모델의 변화가 있을때마다 데이터베이스 스키마에도 해당 변화를 반영해야하는데, 이러한 역할을 하는 것이 마이그레이션이다.

따라서 마이그레이션을 데이터베이스와 연결되는 모델의 변경사항에 따라 버전을 관리해주는 것이라 생각하면 된다. 

## Django에서 Migration을 하는 방법

$ python [manage.py](http://manage.py/) makemigrations

이렇게 하면 migrations 하위 폴더에 0001_initial.py라는 파일이 생성되지만 데이터베이스에 반영되지 않는다. 이 파일은 변경사항을 데이터베이스에 적용할 수 있는 특정 지시사항을 담고 있습니다.

$ python [manage.py](http://manage.py/) migrate

우리가 만들었던 모델이 데이터베이스에 테이블형태로 반영된다. Django는 마이그레이션 파일에 기록된 지시에 따라 데이터베이스 스키마를 업데이트하는 것이다. 

~~약간 git commit과 git push origin 개념과 비슷해보인다.~~