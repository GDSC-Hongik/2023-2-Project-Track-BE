from re import template
from typing import Any, List
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
#from braces.view import LoginRequiredMixin,UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView
from coplate.models import Review,User
from coplate.forms import ReviewForm,ProfileForm
from coplate.functions import confirmation_required_redirect

# Create your views here.
#def index(request):
    
    #request.user는 현재 유저에 대한 모든 필드에 접근할 수 있게 됨 
    #print(request.user.is_authenticated) #유저 이름 출력,is_authenticated는 로그인 되어 있는 상태인지를 판단 
#    return render(request,"coplate/index.html")

#제네릭 뷰 사용
class IndexView(ListView):
    model=Review
    template_name="coplate/index.html"
    context_object_name="reviews"
    paginate_by=4
    ordering=["-dt_created"]
    
class ReviewDetailView(DetailView):
    model=Review
    template_name="coplate/review_detail.html"
    pk_url_kwarg="review_id"

#access mixin은 꼭 제네릭 뷰 왼쪽에 써야 함.(코드가 왼쪽에서 오른쪽으로 실행되기 때문)
class ReviewCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Review
    form_class=ReviewForm
    template_name="coplate/review_form.html"
    
    redirect_unauthenticated_users=True
    raise_exception=confirmation_required_redirect
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form) #오버라이딩
    
    def get_success_url(self):
        return reverse("review-detail",kwargs={"review_id":self.object.id})
    
    def test_func(self,user):
        return EmailAddress.objects.filter(user=user,verified=True).exists()
            
class ReviewUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Review
    form_class=ReviewForm
    template_name="coplate/review_form.html"
    pk_url_kwarg="review_id"
    
    raise_exception=True
    
    
    def get_success_url(self):
        return reverse("review-detail",kwargs={"review_id":self.object.id})
    
    def test_func(self,user):
        review=self.get_object()
        return review.author == user
            

class ReviewDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Review
    template_name="coplate/review_confirm_delete.html"
    pk_url_kwarg="review_id"
    
    raise_exception=True
    
    def get_success_url(self):
        return reverse("index")
    
    def test_func(self,user):
        review=self.get_object()
        return review.author == user

class ProfileView(DetailView):
    model=User
    template_name="coplate/profile.html"
    pk_url_kwarg="user_id"
    context_object_name="profile_user"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user_id=self.kwargs.get("user_id")
        context["user_reviews"]=Review.objects.filter(author__id=user_id).order_by("-dt_created")[:4]
        return context
    
class UserReviewListView(ListView):
    model=Review
    template_name="coplate/user_review_list.html"
    context_object_name="user_reviews"
    paginate_by=4
    
    def get_queryset(self):
        user_id=self.kwargs.get("user_id")
        return Review.objects.filter(author__id=user_id).order_by("-dt_created")
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["profile_user"]=get_object_or_404(User,id=self.kwargs.get("user_id"))
        return context
        
class ProfileSetView(LoginRequiredMixin,UpdateView):
    model=User
    form_class=ProfileForm
    template_name="coplate/profile_set_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("index")

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model=User
    form_class=ProfileForm
    template_name="coplate/profile_update_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile",kwargs={"user_id":self.request.user.id})
    
        
class CustomPasswordChangeView(PasswordChangeView):
    #get_success_url:성공적으로 처리되면 어디로 리디렉션 할지 정해주는 함수
    def get_success_url(self):
        return reverse('profile',kwargs={"user_id":self.request.user.id}) #오버라이딩: 상속받아 기본 클래스의 속성이나 메소드를 바꾸는것
