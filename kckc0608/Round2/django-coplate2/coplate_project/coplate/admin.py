from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import User, Review, Comment, Like

class CommentInline(admin.StackedInline):
    model = Comment
    
class LikeInline(GenericStackedInline):
    model = Like

# 리뷰 admin 페이지에서 댓글을 사용하기 위해, Comment Inline 클래스를 만들어 넘겨줌.
class ReviewAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
        LikeInline,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInline,
    )

class UserInline(admin.StackedInline):
    model = User.following.through # 다대다 관계에서 유저 자체를 설정하려는 경우
    fk_name = "to_user"
    verbose_name = "Follower"
    verbose_name_plural = "Followers"
    

UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'profile_pic', 'intro', 'following',)}),
UserAdmin.inlines = (UserInline,)

admin.site.register(User, UserAdmin)

admin.site.register(Review, ReviewAdmin)

admin.site.register(Comment)

admin.site.register(Like)