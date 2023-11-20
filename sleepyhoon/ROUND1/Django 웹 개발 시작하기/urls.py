from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/',views.index),
    path('menu/<int:pk>/',views.food_detail) # 링크앞에는 항상 foods/가 붙는 것이다. 그래서 foods/menu/pasta로 입력해야함.
]