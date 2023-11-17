from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView

# Create your views here.
def index(request):
    
    #request.user는 현재 유저에 대한 모든 필드에 접근할 수 있게 됨 
    #print(request.user.is_authenticated) #유저 이름 출력,is_authenticated는 로그인 되어 있는 상태인지를 판단 
    return render(request,"coplate/index.html")

class CustomPasswordChangeView(PasswordChangeView):
    #get_success_url:성공적으로 처리되면 어디로 리디렉션 할지 정해주는 함수
    def get_success_url(self):
        return reverse('index') #오버라이딩: 상속받아 기본 클래스의 속성이나 메소드를 바꾸는것
