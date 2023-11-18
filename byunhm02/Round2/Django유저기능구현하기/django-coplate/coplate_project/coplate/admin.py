from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

#admin에 등록,user모델은 Useradmin도 같이 등록해주어야함. 
admin.site.register(User,UserAdmin)

#유저모델에 대한 추가 필드는 기본적으로 어드민 페이지에 나타나지 않기 때문에 따로 어드민페이지에 추가
UserAdmin.fieldsets+=(("Custom fields",{"fields":("nickname",)}),)
