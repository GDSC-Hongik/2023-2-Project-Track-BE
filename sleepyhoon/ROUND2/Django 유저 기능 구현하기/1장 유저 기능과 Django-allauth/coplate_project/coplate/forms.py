from django import forms
from .models import User


# modelform은 model을 정의하면 알아서 form을 만들어준다
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()