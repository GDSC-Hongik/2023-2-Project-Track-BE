from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError

# 그냥 form이 아니라 modelForm을 사용하였다. 기본 틀이 form과 model이 비슷하기 때문이다.
class PostForm(forms.ModelForm):
    # memo = forms.CharField(max_length=80,validators=[validate_symbols])
    class Meta:
        model = Post
        fields = ['title','content'] # '__all__'을 하면 모든 필드 선택됨
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'title',
                'placeholder':'제목을 입력하세요'}),
            'content' : forms.Textarea(attrs={
                'placeholder':'내용을 입력하세요'})
            }
    # form 유효성 검증
    def clean_title(self): # form안의 title에 한해서 유효성 검증 가능
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*은 포함되면 안됩니다')
        return title