# Django 명령어
```python
django-admin --version
```

```python
django-admin startproject costaurant
```

```python
python [manage.py](http://manage.py/) runserver
```

- django에서 manage.py를 이용해서 coffee 라는 이름의 App을 생성하려고 할 때
입력해야 하는 명령어는 무엇일까요? 모두 소문자로 적어주세요.

```python
=> python [manage.py](http://manage.py/) startapp coffee ( 보통은 django-admin startapp coffee)
두 명령어의 차이점??
```

## 주의 사항!!!

> **다른 URL로 이동하기 위한 URL을 적을 때 앞에 슬래시(/)가 있으면** 도메인으로 부터의 경로를 의미합니다. 예를 들어, 현재 [codeit.kr/food/](http://codeit.kr/food/) 에 있다고 하고 아래의 이동하기 링크를 누르면
> 
> 
> ```python
> <a href="/banana/">이동하기</a>
> ```
> 
> 코드의 실행 결과는 [codeit.kr/food/banana/](http://codeit.kr/food/banana/%EA%B0%80) 가 아니라 [codeit.kr/banana/](http://xn--codeit-224xx49h.kr/banana/%EB%A1%9C) 로 이동하게 됩니다.
> 

> **다른 URL로 이동하기 위한 URL을 적을 때 앞에 슬래시(/)가 없으면** 현재 URL 뒤에 이동하는 URL이 연결된 경로가 됩니다.
> 
> 
> 예를 들어,  현재 [codeit.kr/food/](http://codeit.kr/food/) 에 있다고 하고 아래의 이동하기 링크를 누르면
> 
> ```python
> <a href="banana/">이동하기</a>
> ```
> 
> [codeit.kr/food/banana/](http://codeit.kr/food/banana/) 로 이동하게 되는거죠.
> 
- template은 화면 구성을 담당하는 부분(ex: html코드)으로 rendering을 통해 HttpResponse 객체로 변환된다.

> **장고 프로젝트를 windows에서 찾기가 어려운데 wsl에서 해당 디렉토리에 간 후 explorer.exe . 을 실행하면 쉽게 찾을 수 있다. → 내가 참 많이 쓰는 기능**
> 
- python [manage.py](http://manage.py/) makemigrations
python [manage.py](http://manage.py/) migrate → 설명은 아래에 더 자세하게 나왕

```python
Menu.objects.all() : 저장된 모든 데이터 출력 (여기서 Menu는 모델명이다)
Menu.objects.all().values(칼럼명) : 특정 칼럼의 데이터 출력
Menu.objects.order_by('price') : 가격을 기준으로 오름차순 정렬 (내림차순은 -붙임)
Menu.objects.get(조건) : 하나의 데이터 조회
Menu.objects.filter(조건) : 여러 데이터 조회
```

```python
python [manage.py](http://manage.py/) createsuperuser
```

```python
<img src={% get_static_prefix %}{{menu.img_path}}>
```

### Migrate 관련 명령어들

- **makemigrations**

```python
python manage.py makemigrations
```

모델의 변경 사항을 인식해서 새로운 마이그레이션을 만듭니다. 이때 마이그레이션은 각 앱 디렉토리 내 migrations 디렉토리 안쪽에 생성됩니다.

- **migrate**

```
python manage.py migrate
```

생성된 최신 버전의 마이그레이션을 데이터베이스에 반영합니다. 만약 이전 마이그레이션으로 되돌리고 싶다면 python manage.py migrate {앱 이름} {되돌릴 마이그레이션 번호}를 사용할 수 있습니다.

- **showmigrations**

```
python manage.py showmigrations
```

현재 django 프로젝트의 모든 마이그레이션과 반영 상태를 나타냅니다. 만약 특정 앱에 대한 것만 보고 싶다면 python manage.py showmigrations {앱 이름}을 사용할 수 있습니다.

- **sqlmigrate**

```
python manage.py sqlmigrate {앱 이름} {마이그레이션}
```

인수로 넘겨준 마이그레이션이 ORM을 통해 변경된 SQL문을 출력합니다. sqlmigrate를 통해 모델이 의도한 대로 SQL문으로 변경되어 데이터베이스에 반영되었는지 확인할 수 있습니다.