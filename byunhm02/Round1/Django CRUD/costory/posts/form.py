from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError
class PostForm(forms.ModelForm):
    
    
    class Meta:
        model=Post
        fields=['title','content']
        widgets={'title':forms.TextInput(attrs=
            {'class':'title',
             'placeholder':'제목을 입력하세요'}),
             'content':forms.Textarea(attrs={
                 'placeholder':'내용을 입력하세요'})}
        
    def clean_title(self):
        #모든 폼 클래스는 폼 필드를 정의할 때 넣어준 유효성검증을 통과한 데이터가 들어있는 cleaned_data가 있음. 
        title=self.cleaned_data['title']
        #우린 모델 필드를 정의해 주었기 때문에 여기서 cleaned_data[title]에는 유효성검증을 하지 않은 데이터가 있음
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')
        
        return title
            