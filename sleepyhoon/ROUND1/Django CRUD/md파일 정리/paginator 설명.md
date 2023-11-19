# Paginator 정리

## **Django의 페이지네이션**

Django는 페이지네이션을 쉽게 구현할 수 있도록 하는 Paginator를 제공합니다. Paginator는 총 두 개의 파라미터만 넘겨주면 쉽게 정의할 수 있는데 첫 번째 파라미터는 각각의 페이지로 나뉘게 될 데이터의 목록, 두 번째 파라미터는 한 페이지에 보여줄 데이터의 수입니다.

```python

from django.core.paginator import Paginator # Django의 Paginator
from .models import Post # 작성한 모델 클래스

posts = Post.object.all() # 모든 데이터를 가져와서
paginator = Paginator(posts, 6)
# 첫 번째 파라미터 : 페이지로 나뉘게 될 데이터의 목록
# 두 번째 파라미터 :  한 페이지에 보옂루 데이터의 수
```

```python
def post_list(request):
    posts = Post.object.all() 
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.page(page_number) # 페이지 번호에 해당하는 페이지를 가져옴
    return render(request, 'post_list.html', {'page_obj': page_obj})
```

```python
...

{% if page_obj.has_previous %} <!-- 만약 현재 페이지의 이전 페이지가 있다면 -->
    <a href="?page=1">first</a>
    <a href="?page={{ page_obj.previous_page_number }}">prev</a> <!-- 이전 페이지 번호 -->
{% endif %}

<span>
    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
    <!-- page_obj.number : 페이지(page_obj)의 번호 -->
    <!-- page_obj.paginator.num_pages : 페이지를 관리하는 Paginator가 가지고 있는 전체 페이지 수 -->
</span>

{% if page_obj.has_next %} <!-- 만약 현재 페이지의 다음 페이지가 있다면 -->
    <a href="?page={{ page_obj.next_page_number }}">next</a> <!-- 다음 페이지 번호 -->
    <a href="?page={{ page_obj.paginator.num_pages }}">last </a> <!-- 전체 페이지의 개수 = 마지막 페이지 번호 -->
{% endif %}

...
```