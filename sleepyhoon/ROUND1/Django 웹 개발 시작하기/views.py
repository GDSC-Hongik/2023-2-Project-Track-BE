from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import Menu
# Create your views here.
def index(request):
    context=dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context['date'] = today # 사전형으로 선언한다. date는 이름이고 date 변수에 넣을 값은 today
    context['menus'] = menus
    return render(request,'foods/index.html',context=context) # HttpResponse 객체생성

def food_detail(request,pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context['menu'] = menu
    return render(request,'foods/detail.html',context=context)