from django import forms
from .models import User,Review

# 이제 profile 설정에서 nickname을 정하라고 할 거임. 그래서 필요없음
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['nickname']
        
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data['nickname']
#         user.save()
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "restaurant_name",
            "restaurant_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        widgets = {
            "rating":forms.RadioSelect,
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_pic",
            "intro",
        ]
        widgets = {
            "intro":forms.Textarea,
        }
        