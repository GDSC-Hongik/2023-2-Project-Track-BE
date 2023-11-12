from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,unique=True,
                             error_messages={'unique':'이미 있다.'})
    content = models.TextField(validators=[MinLengthValidator(10,'너무 짧아요. 10자 이상 작성하시오.'),
                                           validate_symbols]) # model 유효성 검증
    # 데이터의 생성일 체크, 자동으로 값이 들어가서 따로 입력할 필요없음
    dt_created = models.DateTimeField(verbose_name='Date Created',auto_now_add=True) 
    # 데이터의 마지막 수정일 체크, 자동으로 값이 들어가서 따로 입력할 필요없음
    dt_modified = models.DateTimeField(verbose_name='Date Modified',auto_now=True) 
    
    def __str__(self):
        return self.title