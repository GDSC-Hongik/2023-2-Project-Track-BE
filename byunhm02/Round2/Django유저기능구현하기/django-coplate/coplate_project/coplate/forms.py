from django import forms
from .models import User,Review

#class SignupForm(forms.ModelForm):
#    class Meta:
#        model=User #사용할 model을 불러옴
#        #우리가 추가해준 필드만 명시하면 됨
#        fields=["nickname"]
#        
#    def signup(self, request ,user):
#            #폼에 기입된 데이터는 cleaned_data로 가져올 수 있음
#            user.nickname=self.cleaned_data['nickname']
#            user.save()
    
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=[
            "title",
            "restaurant_name",
            "restaurant_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        widgets={
            "rating": forms.RadioSelect,
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            "nickname",
            "profile_pic",
            "intro",
        ]
        widgets={
            "intro":forms.Textarea
        }