from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloView(request):
    return HttpResponse("<h1>정답입니다!</h1>")