from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm
from allauth.account.views import PasswordChangeView
from allauth.account.models import EmailAddress
from braces.views import LoginRequiredMixin, UserPassesTestMixin

from coplate.functions import confirmation_requried_redirect


class IndexView(ListView):
  model = Review
  template_name = "coplate/index.html"
  context_object_name = "reviews"
  paginate_by = 4
  ordering = ["-dt_created"]


class CustomPasswordChangeView(PasswordChangeView):
  def get_success_url(self):
    return reverse("index")


class ReviewDetailView(DetailView):
  model = Review
  template_name = "coplate/review_detail.html"
  pk_url_kwarg = "review_id"


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView): # 상속 순서대로 접근
  model = Review
  form_class = ReviewForm
  template_name = "coplate/review_form.html"

  redirect_unauthenticated_users = True
  raise_exception = confirmation_requried_redirect
  
  def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)
  
  def get_success_url(self):
    return reverse("review-detail", kwargs={"review_id": self.object.id})
  
  def test_func(self, user):
    return EmailAddress.objects.filter(user=user, verified=True).exists()


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Review
  form_class = ReviewForm
  template_name = "coplate/review_form.html"
  pk_url_kwarg = "review_id"

  raise_exception = True

  def get_success_url(self):
    return reverse("review-detail", kwargs={"review_id": self.object.id})

  def test_func(self, user):
    review = self.get_object()
    return review.author == user


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Review
  template_name = "coplate/review_confirm_delete.html"
  pk_url_kwarg = "review_id"

  raise_exception = True

  def get_success_url(self):
    return reverse("index")

  def test_func(self, user):
    review = self.get_object()
    return review.author == user