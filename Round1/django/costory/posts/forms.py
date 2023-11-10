from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ['title', 'content']
  
  def clean_title(self):
      data = self.cleaned_data["title"]
      if '*' in data:
         raise ValidationError('*는 안됩니다.')
      return data
  