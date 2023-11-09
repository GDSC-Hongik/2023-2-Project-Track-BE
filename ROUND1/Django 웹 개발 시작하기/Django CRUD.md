# Django CRUD

# 데이터(CRUD) - sql문 대신 사용

## **데이터 추가하기 (Create)**

데이터를 추가하기 위해서는 import를 이용해서 먼저 사용할 Model을 불러 와야 합니다.

```python
from {app_name}.models import {model}
```

그 다음 불러온 모델을 이용해서 데이터를 추가하면 되는데 여기에 두가지 방법이 있습니다.

### **Create**

먼저 Create는 데이터 객체를 생성하고 데이터베이스에 반영하는 과정을 한 번에 할 수 있습니다. 생성과 동시에 실제 데이터베이스에 반영이 되는거죠.

```python
data_model = {model}.objects.create( {field_name}=value, ... )
# example
# food = Food.objects.create(price=10000)
```

### **Save**

save를 이용하면 데이터 객체를 생성하는 타이밍과 실제로 데이터베이스에 반영하는 과정을 
분리할 수 있습니다. 아래 코드는 위에서 사용한 Create와 똑같은 기능을 수행합니다.

```python
data_model = {model}( {field_name}=value, ... )
data_model.save()
# example
# food = Food(price=10000)
#   food.save()
```

## **데이터 조회하기 (Read)**

데이터를 데이터베이스로 부터 읽어오는 것은 Django Model Manager인 objects를 통해서 할 수 있습니다. 읽어 온 데이터는 Queryset 이라고 하는 데이터 결과 객체에 들어가며 Queryset은 파이썬의 리스트처럼 사용할 수 있습니다.

### **모든 데이터 조회하기**

데이터 모델의 모든 데이터를 가져오기 위해서는 all()을 사용합니다.

```python
data = {model}.obejcts.all()
```

### **하나의 데이터 조회하기**

하나의 데이터를 가져오기 위해서는 **get()**을 사용합니다. 이때 특정 필드를 전달 인자로 넣어 데이터를 가져오거나 아래에서 설명하는 조건 키워드를 함께 사용할 수 있습니다. get은 하나의 데이터를 조회할 때 라는것을 기억해주세요. 만약 get을 사용했을때 조회 결과가 여러개라면 에러를 내게 됩니다.

```python
data = {model}.objects.get(field=value)
```

### **조건에 맞는 여러 데이터 조회하기**

조건에 맞는 여러 데이터를 조회할 때는 **filter()**를 사용합니다. 필드를 전달 인자로 넣어 해당 필드 조건에 해당하는 모든 데이터를 가져오거나 아래에서 설명하는 조건 키워드를 함께 사용할 수 있습니다.

```python
data = {model}.objects.filter(field=value)
```

### **정렬해서 데이터 조회하기**

데이터를 특정 필드에 따라 정렬해서 조회하고 싶을 때는 **order_by()**를 사용합니다. 이때 두 개 이상의 필드를 함께 사용해서 정렬할 수 있으며 **'-'**를 사용해서 내림차순으로 정렬할 수 있습니다.

```python
data = {model}.objects.order_by('field_1', '-field_2')
# field_1을 기준으로 오름차순으로 정렬하고
# 그 결과를 다시 field_2를 기준으로 내림차순으로 정렬합니다.
```

### **데이터의 개수 세기**

데이터의 개수를 셀 때는 **count()**를 사용합니다.

```python
rows = {model}.objects.count()
```

### **특정 조건을 제외한 데이터 조회하기**

특정 조건을 제외한 데이터를 조회하고 싶을 때는 **exclude()**를 사용해 보세요.

```python
data = {model}.objects.exclude(field=value)
# 특정 field가 value인 데이터를 제외한 모든 데이터를 조회합니다.
```

### **체인으로 연결해서 조회하기**

여러가지 데이터 조회를 체인처럼 연결해서 사용할 수 있습니다. 아래에서 배우는 조건 키워드도 모두 한 번에 엮어서 사용할 수 있습니다.

```python
data = {model}.objects.filter(price=10000).order_by('name')
# 가격(price)이 10,000원인 데이터를 이름(name)으로 정렬해서 조회합니다.
```

```python
data = {model}.objects.filter(price=10000)
data = data.order_by('name')
# 이렇게 적어도 위와 똑같은 명령을 수행합니다.
```

2가지 방법이 존재하는데 아래 방법을 더 추천함. 위 방법으로 실행한다고 해서 더 빨라지지도 않기 때문에 가독성 때문이라도 아래 방법을 이용해서 검색하는게 맞다고 본다.

### **조건 키워드**

모든 데이터 조회는 조건 키워드를 함께 사용하여 조회할 수 있으며 **{field_name}__{keyword}={condition}** 형태로 사용합니다. 아래는 몇가지 조건 키워드의 예시입니다.

- **__exact, __iexact**

__exact는 대소문자를 구분해서 조건과 정확히 일치 하는지를 체크하며
__iexact는 대소문자를 구분 하지 않고 일치하는 지를 체크합니다.

```python
data = {model}.objects.filter(name__iexact='chicken')
# 음식의 이름(name)이 'chicken'인 데이터를 모두 조회합니다.
# 단, 대소문자를 구분하지 않습니다.
```

- **__contains, __icontains**

지정한 문자열을 포함 하는지를 체크합니다. 
마찬가지로 __icontains는 대소문자를 구분하지 않고 체크합니다.

```python
data = {model}.objects.filter(name__contains='chicken')
# 음식의 이름(name)에 'chicken'이 포함된 모든 데이터를 조회합니다.
# 단, 대소문자를 구분합니다. (__contains)
```

- **__range**

지정한 범위 내에 포함 되는지 체크합니다.

날짜, 숫자 문자 등 모든 데이터의 범위를 사용할 수 있으며 파이썬의 range와 비슷합니다.

```python
data = {model}.objects.filter(price__range=(1000,5000))
# 가격(price)이 1000원~5000원인 모든 데이터를 조회합니다.
```

```python
import datetime
start_date = datetime.date(2020,8,12)
end_date = datetime.date(2020,9,12)
data = {model}.objects.filter(pub_date__range=(start_date,end_date))
# 생성일(pub_date)이 2020-08-12~2020-09-12인 모든 데이터를 조회합니다.
```

이밖에도 많은 조건 키워드가 있습니다.

- **__lt , __gt, __lte, __gte**

미만 (less-than), 초과 (greater-than)
이하 (less-than-or-equal), 이상(greater-than-or-equal)인 데이터를 조회합니다.

```python
data = {model}.objects.filter(age__gt=25)
```

- **__in**

주어진 리스트 안에 존재하는 자료를 조회합니다.

```python
data = {model}.objects.filter(age__in=[21,25,27])
```

추가 조건이 궁금하다면 이래 참조.
**https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups**

## **데이터 수정하기**

데이터를 수정하기 위해서는 수정할 데이터 객체를 가져온 다음 원하는 필드를 수정하고 save()를 호출하여 데이터베이스에 반영하면 됩니다.

```python
data = {model}.objects.get(id=1)
data.name = 'Woojae'
data.save()
```

## **데이터 삭제하기**

데이터를 삭제하기 위해서는 삭제할 데이터 객체를 가져온 다음 delete()를 호출하면 됩니다.
```python
data = {model}.objects.get(id=3)
data.delete()
```