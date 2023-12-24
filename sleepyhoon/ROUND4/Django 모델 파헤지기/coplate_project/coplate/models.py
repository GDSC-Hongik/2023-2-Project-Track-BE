from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from .validators import validate_no_special_characters, validate_restaurant_link


class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')

    intro = models.CharField(max_length=60, blank=True)

    following = models.ManyToManyField('self',symmetrical=False, \
        blank=True, related_name='followers') # User간의 follow. null 옵션없이 null 허용
    
    def __str__(self):
        return self.email



class Review(models.Model):
    title = models.CharField(max_length=30)

    restaurant_name = models.CharField(max_length=20)

    restaurant_link = models.URLField(validators=[validate_restaurant_link])

    RATING_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=None)

    image1 = models.ImageField(upload_to='review_pics')

    image2 = models.ImageField(upload_to='review_pics', blank=True)

    image3 = models.ImageField(upload_to='review_pics', blank=True)

    content = models.TextField()

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,\
        related_name='reviews')
    
    # like class가 맨 밑에 존재하기 때문에 문자열로 작성해줘야함.
    likes = GenericRelation('Like',related_query_name='review') # review.likes

    def __str__(self):
        return self.title
    
    class Meta: # review 모델 자체에 대한 옵션의 default값을 만들 수 있음
        ordering = ['-dt_created']
    
class Comment(models.Model):
    content = models.TextField(max_length=500,blank=False)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User,on_delete=models.CASCADE,\
        related_name='comments') # user.comments로 접근 가능
    
    review = models.ForeignKey(Review,on_delete=models.CASCADE,\
        related_name='comments') # review.comments로 접근 가능
    
    # like class가 맨 밑에 존재하기 때문에 Like를 문자열로 작성해줘야함.
    likes = GenericRelation('Like',related_query_name='review') # comment.likes
    
    def __str__(self):
        return self.content[:30]
    
    class Meta: # review 모델 자체에 대한 옵션의 default값을 만들 수 있음
        ordering = ['-dt_created']
        
class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,\
        related_name='likes') # user.likes로 접근 가능
    
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    
    object_id = models.PositiveIntegerField()
    
    liked_object = GenericForeignKey() # 위에서 content_type, object_id 정의해주면 매개변수 필요 x
    
    def __str__(self):
        return f"({self.user},{self.liked_object})"
    
    class Meta:
        unique_together = ['user', 'content_type', 'object_id'] # 같은 튜플 생성 안됌
