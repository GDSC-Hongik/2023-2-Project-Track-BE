from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import CreateView,\
    ListView, DetailView,UpdateView,DeleteView,RedirectView
from django.urls import reverse
from .models import Post
from .forms import PostForm

# def index(request):
#     return redirect('post-list')

# 오히려 함수형 view가 가독성 좋은 경우
class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'

class PostListView(ListView):
    model = Post
    # template_name = 'posts/post_list.html' <모델명>_list를 이름으로 하면 알아서 찾아줌
    context_object_name = 'posts'
    ordering=['-dt_created']
    paginate_by = 6
    # page_kwarg = 'page' # 쿼리 스트링에서 현재 페이지에 해당하는 데이터를 가져오기 위한 키워드.
    # 이미 알아서 post_list.html에서 ?page=1 이런 식으로 사용하고 있어서 default 값으로 가능하다.

class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html' <모델명>_detail을 이름으로 하면 알아서 찾아줌
    # pk_url_kwarg = 'post_id' # view에 넘겨주는 키의 값, 기본값은 pk이여서 urls.py에서 post_id -> pk로 변경시 생략가능
    # context_object_name = 'post' # 모델명을 소문자로 적어준 값이 default이므로 생략가능

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm # CreateView에서 사용할 폼 클래스. 기본값은 form
    # template_name = 'posts/post_form.html' <모델명>_form 이면 안써줘도 됨
    
    
    def get_success_url(self): # 객체가 생성되고 이동할 url 찾기
        return reverse('post-detail', kwargs={'pk': self.object.id}) # 위에서 post_id를 pk로 변경했음

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm # 기본값은 form
    # template_name = 'posts/post_form.html' <모델명>_form 이면 안써줘도 됨
    # pk_url_kwarg = 'pk' pk면 삭제가능
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html' <모델명>_comfirm_delete 이면 안써줘도됨
    # pk_url_kwarg = 'pk' pk로 바꿔주고 삭제처리
    # context_object_name = 'post' 모델명의 소문자꼴이면 삭제가능.
    
    def get_success_url(self):
        return reverse('post-list')