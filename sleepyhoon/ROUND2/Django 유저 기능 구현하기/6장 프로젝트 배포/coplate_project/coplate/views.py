from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import ListView,DetailView,\
    CreateView,UpdateView,DeleteView
from braces.views import LoginRequiredMixin,UserPassesTestMixin
from allauth.account.views import EmailAddress
from coplate.models import Review,User
from coplate.forms import ReviewForm,ProfileForm
from coplate.functions import confirmation_required_redirect

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

# mixin을 매개변수에 넣을때는 반드시 mixin을 왼쪽에 위치시켜야한다.
class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView): # 로그인에서 mixin을 넣어줌(접근제어 필요)
    model = Review
    form_class = ReviewForm
    template_name = "coplate/review_form.html" # 기본적으로 form이라는 변수로 전달해준다.
    
    redirect_unauthenticated_users = True # 로그인 유무에 따라 행동이 다름
    raise_exception = confirmation_required_redirect # 로그인은 했는데 이메일 인증 안한 사람
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # author도 review obj안에 저장할 수 있음.

    def get_success_url(self):
        return reverse('review-detail', kwargs={"review_id":self.object.id}) # review_id값 전달
    
    def test_func(self, user):
        # "유저가 등록되어 있고, 인증된 것이 존재한다면" 이라고 해석 -> 조건을 충족하는지 확인해줌
        return EmailAddress.objects.filter(user=user, verified = True).exists()
    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = "review_id"
    
    raise_exception = True # 잘 못된 접근인 경우 403 에러를 출력
    # redirect_unauthenticated_users = False => 기본값이 False여서 생략해도됨
    
    def get_success_url(self):
        return reverse('review-detail', kwargs={"review_id":self.object.id}) # review_id값 전달
    
    def test_func(self, user):
        review = self.get_object() # review 가져오기
        return review.author == user
      
      
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'coplate/review_confirm_delete.html'
    pk_url_kwarg = "review_id"
    
    raise_exception = True # 잘 못된 접근인 경우 403 에러를 출력
    
    def get_success_url(self):
        return reverse('index')
    
    def test_func(self, user):
        review = self.get_object() # review 가져오기
        return review.author == user
      
# 어떤 유저 1명의 정보를 template에 전달해준다.
class ProfileView(DetailView):
    model = User
    template_name = "coplate/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user" # 기본값은 user

    # 추가적으로 user가 작성한 리뷰를 가져온다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 리뷰 넣어주기
        user_id = self.kwargs.get("user_id")
        context["user_reviews"] = Review.objects.filter(author__id = user_id).order_by(
            "-dt_created"
         )[:4]
        return context
    
# 리뷰 리스트 자체를 template에 전달해준다.
class UserReviewListView(ListView): # listview는 모든 리뷰를 가져오기 때문에 범위 수정 필요
    model = Review
    template_name = 'coplate/user_review_list.html'
    context_object_name = "user_reviews"
    paginate_by = 4
    
    # 해당 함수를 오버라이딩 하여 특정 유저의 리뷰만 전달하도록 하였다. 여러개여서 queryset
    # 해당 함수의 return 값이 template에 최종 전달된다.
    def get_queryset(self):
        user_id = self.kwargs.get("user_id") # 해당 유저에 해당하는 리뷰만 담을 거임
        return Review.objects.filter(author__id=user_id).order_by("-dt_created")

    # 해당 뷰에서는 template에 review만 전달해주고, user에 관련된 정보는 전달해주지 않음
    # template 에서는 user에 관련된 정보가 필요하기 때문에, 따로 전달을 해주어야 함.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(
            User, id=self.kwargs.get("user_id")
        ) # 해당되는 유저가 없으면 404
        return context
    
# 새로 profile을 작성하는 것이여서 updateview 필요하다.
# but 업데이트할 user의 id가 url로 전달되지 않음. 업데이트할 user의 정보를 필요로함
# get_object 함수를 사용하여 접근한다.
class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "coplate/profile_set_form.html"
    
    # get_queryset 함수와 비슷한 역할이나, 1개만 전달하면 되므로 get_object을 사용
    # 현재 로그인한 user를 가져와야한다. 
    def get_object(self, queryset=None):
        return self.request.user
    
    # 업데이트하고 나서 이동할 url을 설정 해줘야한다.
    def get_success_url(self):
        return reverse('index')
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "coplate/profile_update_form.html"
    
    # get_queryset 함수와 비슷한 역할이나, 1개만 전달하면 되므로 get_object을 사용
    # 현재 로그인한 user를 가져와야한다. 
    def get_object(self, queryset=None):
        return self.request.user
    
    # 업데이트하고 나서 이동할 url을 설정 해줘야한다.
    def get_success_url(self):
        return reverse('profile', kwargs=({"user_id":self.request.user.id}))

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs=({"user_id":self.request.user.id}))
    

