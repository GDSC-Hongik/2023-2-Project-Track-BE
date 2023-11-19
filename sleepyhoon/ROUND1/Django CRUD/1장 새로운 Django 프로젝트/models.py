from django.db import models

# Create your models here.
class Post(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50)
    # 최대 길이 선언 x
    content = models.TextField()
    # 데이터의 생성일 체크, 자동으로 값이 들어가서 따로 입력할 필요없음
    dt_created = models.DateTimeField(verbose_name='Date Created',auto_now_add=True) 
    # 데이터의 마지막 수정일 체크, 자동으로 값이 들어가서 따로 입력할 필요없음
    dt_modified = models.DateTimeField(verbose_name='Date Modified',auto_now=True) 
    
    def __str__(self):
        return self.title