from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters,validate_restaurant_lisk
# model 정의하고 나서 꼭 makemigrations 랑  migrate 실행하자. 등록해야 반영이 된다.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True,
        error_messages={'unique': '이미 사용중인 닉네임입니다'},
        validators=[validate_no_special_characters],                        
    )
    
    def __str__(self):
        return self.email
    
class Review(models.Model):
    title = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=20)
    restaurant_link = models.URLField(validate_restaurant_lisk) # 카카오,네이버 링크만 허용하도록 validator 설정
    
    Rating_choices=[
        (1,"★"),(2,"★★"),(3,"★★★"),(4,"★★★★"),(5,"★★★★★"), # select box가 default
    ]
    
    rating = models.IntegerField(choices=Rating_choices, default=None)
    
    image1 = models.ImageField(upload_to="review_pics")
    image2 = models.ImageField(upload_to="review_pics",blank=True)
    image3 = models.ImageField(upload_to="review_pics",blank=True) 
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True) # 생성된 시간 저장
    dt_modified = models.DateTimeField(auto_now=True) # 수정된 시간 저장
    
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자 삭제되면 관련 리뷰 전부 삭제
    
    def __str__(self):
        return self.title