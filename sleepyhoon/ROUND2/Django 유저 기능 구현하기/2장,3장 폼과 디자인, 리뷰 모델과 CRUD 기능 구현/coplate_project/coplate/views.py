from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import ListView,DetailView,\
    CreateView,UpdateView,DeleteView
from coplate.models import Review
from coplate.forms import ReviewForm

# @@ 현재 버전에서는 로그아웃상태에서도 리뷰작성이 가능함. 다음 챕터에서 이거 개선할듯@@

# 제네릭 뷰 사용
class IndexView(ListView):
    model = Review
    template_name = "coplate/index.html"
    context_object_name = "reviews" # 기본값은 review_list
    paginate_by = 4
    ordering = ["-dt_created"] # 내림차순으로 정렬
    
    
class ReviewDetailView(DetailView):
    model = Review
    template_name = "coplate/review_detail.html"
    pk_url_kwarg = "review_id" # urls.py에서 사용한 이름 그대로 사용
    # context_object_name = "review" 가 기본값이여서 생략함

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "coplate/review_form.html" # 기본적으로 form이라는 변수로 전달해준다.
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # author도 review obj안에 저장할 수 있음.

    def get_success_url(self):
        return reverse('review-detail', kwargs={"review_id":self.object.id}) # review_id값 전달
    
    
    
class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = "review_id"
    
    def get_success_url(self):
        return reverse('review-detail', kwargs={"review_id":self.object.id}) # review_id값 전달
      
      
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'coplate/review_confirm_delete.html'
    pk_url_kwarg = "review_id"
    
    def get_success_url(self):
        return reverse('index')
      
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
    

