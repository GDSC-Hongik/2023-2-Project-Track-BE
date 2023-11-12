from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse
from .models import Post
from .forms import PostForm

class PostCreateView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'posts/post_form.html' # context 는 알아서 "form" 이라는 키워드로 넘겨줌

  def get_success_url(self) -> str:
    return reverse('post-detail', kwargs={'post_id': self.object.id}) ## 리다이렉트 주소 및 인자 전달


class PostListView(ListView):
  model = Post
  template_name = 'posts/post_list.html'
  context_object_name = 'posts'
  ordering = ['-dt_created'] # 최근 작성순으로 정렬 (날짜 역순)
  paginate_by = 6
  page_kwarg = 'page'


class PostDetailView(DetailView):
  model = Post
  template_name = 'posts/post_detail.html'
  pk_url_kwarg = 'post_id'
  context_object_name = 'post'


# def post_update(request, post_id):
#   post = get_object_or_404(Post, id=post_id)

#   if request.method == 'POST':
#     post_form = PostForm(request.POST, instance=post) # 새로운 Post 객체를 만드는 게 아니므로, 기존 인스턴스를 넘겨줌.
#     if post_form.is_valid():
#       post_form.save()
#       return redirect('post-detail', post_id = post.id)
#   else:
#     post_form = PostForm(instance=post) # 기존 post 데이터 내용을 담아서 폼 생성
#   return render(request, 'posts/post_form.html', {'form': post_form})

class PostUpdateView(UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'posts/post_form.html'
  pk_url_kwarg = 'post_id'
  
  def get_success_url(self) -> str:
    return reverse('post-detail', kwargs={'post_id': self.object.id})


def post_delete(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  if request.method == 'POST':
    post.delete()
    return redirect('post-list')

  return render(request, 'posts/post_confirm_delete.html', {'post':post})


def index(request):
  return redirect('post-list')
