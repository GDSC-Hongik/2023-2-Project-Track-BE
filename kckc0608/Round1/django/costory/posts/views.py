from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
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


class PostUpdateView(UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'posts/post_form.html'
  pk_url_kwarg = 'post_id'
  
  def get_success_url(self) -> str:
    return reverse('post-detail', kwargs={'post_id': self.object.id})


class PostDeleteView(DeleteView):
  model = Post
  template_name = 'posts/post_confirm_delete.html'
  pk_url_kwarg = 'post_id'
  context_object_name = 'post'

  def get_success_url(self) -> str:
    return reverse('post-list')


def index(request):
  return redirect('post-list')
