from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import PostForm

# Create your views here.
def post_list(request):
  posts = Post.objects.all()
  paginator = Paginator(posts, 6)
  curr_page_number = request.GET.get('page') # get querystring data
  if curr_page_number is None:
    curr_page_number = 1

  page = paginator.page(curr_page_number)
  return render(request, 'posts/post_list.html', context={"page": page})


def post_detail(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  return render(request, 'posts/post_detail.html', context={"post": post})


def post_create(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      new_post = post_form.save()
      return redirect('post-detail', post_id = new_post.id)
  else:
    post_form = PostForm()
  return render(request, 'posts/post_form.html', {"form": post_form})


def post_update(request, post_id):
  post = get_object_or_404(Post, id=post_id)

  if request.method == 'POST':
    post_form = PostForm(request.POST, instance=post) # 새로운 Post 객체를 만드는 게 아니므로, 기존 인스턴스를 넘겨줌.
    if post_form.is_valid():
      post_form.save()
      return redirect('post-detail', post_id = post.id)
  else:
    post_form = PostForm(instance=post) # 기존 post 데이터 내용을 담아서 폼 생성
  return render(request, 'posts/post_form.html', {'form': post_form})


def post_delete(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  if request.method == 'POST':
    post.delete()
    return redirect('post-list')

  return render(request, 'posts/post_confirm_delete.html', {'post':post})


def index(request):
  return redirect('post-list')
