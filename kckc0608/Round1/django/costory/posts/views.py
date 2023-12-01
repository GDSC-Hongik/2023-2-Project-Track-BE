from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from django.urls import reverse
from .models import Post
from .forms import PostForm

class PostCreateView(CreateView):
  model = Post
  form_class = PostForm

  def get_success_url(self) -> str:
    return reverse('post-detail', kwargs={'pk': self.object.id}) ## 리다이렉트 주소 및 인자 전달


class PostListView(ListView):
  model = Post
  ordering = ['-dt_created'] # 최근 작성순으로 정렬 (날짜 역순)
  paginate_by = 6


class PostDetailView(DetailView):
  model = Post


class PostUpdateView(UpdateView):
  model = Post
  form_class = PostForm
  
  def get_success_url(self) -> str:
    return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
  model = Post

  def get_success_url(self) -> str:
    return reverse('post-list')


# def index(request):
#   return redirect('post-list')
class IndexRedirectView(RedirectView):
  pattern_name = 'post-list'
