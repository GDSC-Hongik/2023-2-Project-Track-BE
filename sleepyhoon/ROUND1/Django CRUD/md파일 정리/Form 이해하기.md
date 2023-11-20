# ****HTML Form****

폼은 웹 페이지에서 사용자의 데이터를 입력받을 수 있는 입력 양식을 말한다. 보통 기본 폼의 형식은 Django에서 제공하지만, 기본적인 html 폼의 형식을 알고있으면 도움이 된다.

### **label과 input**

폼은 form태그 안에 사용자의 입력을 받는 input태그와 설명을 위한 label태그의 쌍으로 구성됩니다.

```html

<form>
    <lable>이름</lable>
    <input type="text">
</form>

```

https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4134&directory=Untitled.png&name=Untitled.png

### **for & id**

각각의 input태그와 label태그를 묶어주기 위해서 **label태그에는 for 속성, input태그에는 id**가 사용됩니다.

```html

<form>
    <label for="title">제목</label>
    <input type="text" id="title">
</form>

```

만약 여기에서 for와 id 속성을 적어주고 싶지 않다면 label 태그로 input태그를 감싼 형태를 사용하면 됩니다.

```html

<form>
    <label>제목
        <input type="text">
    </label>
</form>

```

### **name**

name은 입력된 데이터를 서버로 전송할 때, 서버에서 각각의 데이터를 구분하기 위한 속성으로 name 속성이 있는 양식 요소만 값이 서버로 전달됩니다.

```html

<form>
    <label for="title">제목</label>
    <input type="text" id="title" name="title">
</form>

```

### **type**

**type은 입력할 값에 따른 유형**을 나타내는 속성입니다. 이 type에 따라 사용자가 브라우저에서 값을 입력하는 형식인 위젯(widget)이 달라집니다. 자주 사용되는 type은 아래와 같습니다.

- email

```html

<label for="email">이메일</label>
<input type="email" id="email" name="email">

```


- password

```html

<label for="pwd">비밀번호</label>
<input type="password" id="pwd" name="pwd">

```



- button

```html

<input type="button" value="버튼입니다">

```


- radio

```html

<input type="radio" id="male" name="gender" value="male">
<label for="male">남자</label><br>
<input type="radio" id="female" name="gender" value="female">
<label for="female">여자</label><br>
<input type="radio" id="other" name="gender" value="other">
<label for="other">기타</label>

```


- checkbox

```html

<input type="checkbox" id="lang1" name="lang1" value="Python">
<label for="lang1">파이썬(Python)</label><br>
<input type="checkbox" id="lang2" name="lang2" value="JAVA">
<label for="lang2">자바(JAVA)</label><br>
<input type="checkbox" id="lang3" name="lang3" value="Go">
<label for="lang3">고(Go)</label><br>

```


- date

```html

<label for="birthday">생년월일</label>
<input type="date" id="birthday" name="birthday">

```



- file

```html

<label for="userfiles">파일선택</label>
<input type="file" id="userfiles" name="userfiles" multiple>

```



- submit

```html

<input type="submit" value="전송하기">

```



## **form 속성**

form에는 입력된 데이터를 전송할 서버의 URL을 지정하는 action과 http 전달 방식을 지정해 주는 method 속성이 있습니다. 그 중에서 가장 대표적인 get, post를 알아봅시다. 간단히 말하면 get은 서버에 정보를 요청해 가져오는 것이고, post는 서버의 정보를 변경하려는 요청을 할 때 사용한다. get이 주로 조회(R)에 쓰이고 post가 생성, 삭제, 수정 등 (C,U,D)에 쓰인다

```html

<form action="register" method="post">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <input type="submit" value="제출하기">
</form>

```

## **GET과 POST**

GET 방식으로 지정하면 유저가 데이터를 입력하고 전송했을 때 URL 뒤에 쿼리 스트링(Query String) 형태로 데이터가 전달됩니다.

```html

<form action="/register" method="get">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <label for="email">이메일</label>
    <input type="email" id="email" name="email">
    <input type="submit" value="제출하기">
</form>

```

```html

http://www.codeit-django.com/register?name=우재&email=woojae@codeit.kr

```

POST 방식은 전송되는 URL에는 표시되지 않고 서버로 전송하는 메세지 안쪽에 데이터를 넣어서 전달합니다. 이 부분에 대해서는 조금 더 나중에 자세하게 다루겠습니다.

```html

<form action="/register" method="post">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <label for="email">이메일</label>
    <input type="email" id="email" name="email">
    <input type="submit" value="제출하기">
</form>

```

```html

http://www.codeit-django.com/register

```

### Form 처리 과정?

Form은 유저가 GET 방식으로 폼을 요청하면 서버에서 빈 폼을 제공하고, 유저가 데이터를 입력한 후 POST 방식으로 폼을 서버로 전달하면, 서버에서 유효성 검증을 거친 후 데이터를 처리하는 방식으로 처리됩니다.

# **Django Form Field**

Django 폼(Form)을 작성할 때 가장 중요한 부분이 바로 데이터에 맞는 폼 필드를 작성하는 것입니다. Django는 입력 데이터에 따라 사용할 수 있는 여러 내장 폼 필드를 제공하는데, 각각의 폼 필드는 그에 맞는 입력 위젯을 기본으로 가지고 있습니다. 아래는 Django에서 제공하는 몇 가지 필드 목록과 옵션들 입니다.

| 필드 | 설명 | 옵션 | 기본 위젯 |
| --- | --- | --- | --- |
| CharField | 문자열 입력을 위한 필드입니다. | max_length : 최대 길이 설정 min_length : 최소 길이 설정 strip : 문자열 앞뒤 공백을 제거합니다. (기본값: True) empty_value : 비어 있는 값을 나타낼 값 (기본값: 빈 문자열) | TextInput |
| EmailField | 이메일 입력을 위한 필드입니다. | CharField와 같은 옵션인자를 사용합니다. | EmailInput |
| IntegerField | 정수 입력을 위한 필드입니다. | max_value : 최댓값 설정 min_value : 최솟값 설정 | NumberInput |
| BooleanField | True, False 입력을 위한 필드입니다. (기본적으로 입력을 위해 체크박스가 사용됩니다.) | 체크박스가 빈 값일 경우 False로 처리됩니다. | CheckboxInput |
| ChoiceField | 주어진 값 안에서 하나를 선택할 수 있는 형식의 필드입니다. | choices : 선택 항목 들의 목록 인자로 각 선택 목록은 튜플 형식을 사용합니다. 예시: options = [('1', 'male'), ('2', 'female), ('3', 'other')] | Select |
| MultipleChoiceField | 주어진 보기에서 여러개를 선택할 수 있는 형식의 필드입니다. | ChoiceField와 같은 옵션인자를 사용합니다. | SelectMultiple |
| DateField | 날짜 형식을 입력 받는 필드입니다. | input_formats : 날짜의 형식을 지정합니다. (https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-DATE_INPUT_FORMATS) | DateInput |
| TimeField | 시간 형식을 입력받는 필드입니다. | DateField와 같은 옵션인자를 사용합니다. | TimeInput |
| DateTimeField | 날짜/시간 형식을 입력 받는 필드입니다. | DateField와 같은 옵션인자를 사용합니다. | DateTimeInput |

아래는 필드를 정의할 때 사용할 수 있는 필드 옵션들 입니다.

| 인수 | 설명 |
| --- | --- |
| required | 필수적으로 입력해야 하는 항목 인지를 결정합니다. 기본값은 True이며 False일 경우 비워두는 것을 허용합니다. |
| label | 해당 필드의 label 항목에 적힐 이름을 지정합니다. 만약 지정하지 않을 경우 폼 필드를 지정한 변수명의 첫 글자를 대문자로, 밑줄(_)이 있다면 띄어쓰기로 변경하여 label 값으로 사용합니다. |
| label_suffix | 기본적으로 label 다음 콜론(:)이 붙어서 표시되는데 이 값을 변경합니다. |
| initial | 해당 필드에 초기값을 줄 때 사용합니다. |
| widget | 해당 필드가 사용할 사용자 입력 UI, 즉 위젯을 지정합니다. 기본적으로 각 데이터 항목에 맞는 기본 위젯이 설정되어 있습니다. |
| help_text | 입력에 도움이 되는 문자열을 입력 필드 밑에 표시합니다. |
| validators | 유효성 검증을 위한 검증 목록을 리스트 형태로 작성합니다. |
| disabled | 필드의 편집 가능 여부를 결정합니다. 기본 값은 False 이며 True일 경우 해당 필드가 보이지만 편집할 수 없습니다. |

## Model form?

폼 작성의 경우 forms.py를 작성해서

```python
from django import forms

# 기본적으로 CharField의 경우 한줄입력을 받는 widget이 default임. model 작성 양식과 거의 비슷한듯.
class PostForm(forms.Mo):
    title = forms.CharField(max_length=50, label='제목')
    content = forms.CharField(label='내용',widget=forms.Textarea)
```

이런 식으로 표현을 했었는데, modelform을 사용하면 더 간편하게

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content'] # '__all__'을 하면 모든 필드 선택됨
```

아래와 같이 구현 가능하다. 이게 가능한 이유는 form과 model의 구성이 거의 동일하기 때문인데 model에서 내가 원하는 필드만 골라서 form을 만드는 것도 가능하다. 이렇게 만든 것을 model form 이라고 한다.

## Form 출력하기

```python
<!-- posts/post_form.html -->

<form method="post" action="{% url 'post-create' %}">{% csrf_token %}
  {{ form.as_ul }}
  <button type="submit">Submit</button>
</form>
```

form을 ul태그를 이용해서 전부 출력해준다. 근데 모양새가 안 이쁜 경우가 있음.