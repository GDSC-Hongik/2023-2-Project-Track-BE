from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ['title', 'content']
    widgets = {
       "title": forms.TextInput(attrs={
          'class': 'title',
          'placeholder': '제목을 입력하세요.',
        }),
        "content": forms.Textarea(attrs={
           'placeholder': '내용을 입력하세요.',
        })
    }
  
  def clean_title(self):
      data = self.cleaned_data["title"]
      if '*' in data:
         raise ValidationError('*는 안됩니다.')
      return data
  