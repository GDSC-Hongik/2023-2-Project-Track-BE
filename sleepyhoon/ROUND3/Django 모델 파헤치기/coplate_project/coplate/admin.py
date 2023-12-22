from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import User, Review, Comment, Like


class CommentInline(admin.StackedInline):
    model = Comment

# 제네릭 관계로 되어 있어서 GenericStackedInline 사용해야함.
class LikeInline(GenericStackedInline):
    model = Like

class UserInline(admin.StackedInline):
    model = User.following.through
    fk_name = 'to_user' # self인 경우에만 표시
    verbose_name = 'Follower'
    verbose_name_plural = 'Followers'
    
UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'profile_pic', 'intro','following',)}),
UserAdmin.inlines = (UserInline,)

# admin 페이지에서 리뷰에 들어가서 like 와 comment를 inline으로 가능하게 해줌.
class ReviewAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
        LikeInline,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInline,
    )


admin.site.register(User, UserAdmin)

admin.site.register(Review,ReviewAdmin)

admin.site.register(Comment,CommentAdmin)

admin.site.register(Like)
