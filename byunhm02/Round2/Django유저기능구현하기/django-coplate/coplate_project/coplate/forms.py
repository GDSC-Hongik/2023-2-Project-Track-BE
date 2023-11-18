from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model=User #사용할 model을 불러옴
        #우리가 추가해준 필드만 명시하면 됨
        fields=["nickname"]
        
    def signup(self, request ,user):
            #폼에 기입된 데이터는 cleaned_data로 가져올 수 있음
            user.nickname=self.cleaned_data['nickname']
            user.save()
    
    
