from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Review
# Register your models here.
admin.site.register(User,UserAdmin) # user는 useradmin을 추가해줘야함.
UserAdmin.fieldsets += (("Custom fields",{"fields": ("nickname",)}),) # custom fields 라는 section 아래에 nickname field 추가

admin.site.register(Review)