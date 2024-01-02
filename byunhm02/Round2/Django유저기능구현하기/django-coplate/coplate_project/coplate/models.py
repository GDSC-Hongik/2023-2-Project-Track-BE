from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters,validate_restaurant_link

# Create your models here.
class User(AbstractUser):
    nickname=models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique':'이미 사용중인 닉네임입니다.'},
    )
    
    profile_pic=models.ImageField(
        default="default_profile_pics.jpg",
        upload_to="profile_pics"
    )
    
    intro=models.CharField(max_length=60,blank=True)
    
    def __str__(self):
        return self.email
    
class Review(models.Model):
    title=models.CharField(max_length=30)
    restaurant_name=models.CharField(max_length=20)
    restaurant_link=models.URLField(validators=[validate_restaurant_link]) #필드에 넣을 값이 url형태 아니면 오류
    
    
    RATING_CHOICES=[
        (1,"★"),
        (2,"★★"), #앞쪽 값은 모델에 저장, 뒷 값은 화면에 보이는 역할 
        (3,"★★★"),
        (4,"★★★★"),
        (5,"★★★★★"),
    ]
    rating=models.IntegerField(choices=RATING_CHOICES,default=None)
    
    image1=models.ImageField(upload_to="review_pics")
    image2=models.ImageField(upload_to="review_pics",blank=True)
    image3=models.ImageField(upload_to="review_pics",blank=True)
    content=models.TextField()#TextField 길이 제한 없는 필드
    dt_created=models.DateTimeField(auto_now_add=True)#auto_now_add=True모델이 생성된 시간 넣어줌
    dt_updated=models.DateTimeField(auto_now=True)#auto_now=True는 모델이 마지막으로 저장된 시간을 필드에 넣어줌
    
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    