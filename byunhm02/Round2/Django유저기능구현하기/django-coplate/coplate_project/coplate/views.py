
from typing import List
from django.shortcuts import render
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
from coplate.models import Review
from coplate.forms import ReviewForm
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

class CustomPasswordChangeView(PasswordChangeView):
    #get_success_url:성공적으로 처리되면 어디로 리디렉션 할지 정해주는 함수
    def get_success_url(self):
        return reverse('index') #오버라이딩: 상속받아 기본 클래스의 속성이나 메소드를 바꾸는것
