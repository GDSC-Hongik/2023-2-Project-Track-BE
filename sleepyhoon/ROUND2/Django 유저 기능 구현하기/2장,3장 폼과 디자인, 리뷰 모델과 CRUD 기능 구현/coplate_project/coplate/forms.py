from django import forms
from .models import User,Review

# modelform은 model을 정의하면 알아서 form을 만들어준다
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname']
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()
        
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
        