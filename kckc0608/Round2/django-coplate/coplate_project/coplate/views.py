from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import Review
from allauth.account.views import PasswordChangeView


class IndexView(ListView):
  model = Review
  template_name = "coplate/index.html"
  context_object_name = "reviews"
  paginate_by = 4
  ordering = ["-dt_created"]


class CustomPasswordChangeView(PasswordChangeView):
  def get_success_url(self):
    return reverse("index")