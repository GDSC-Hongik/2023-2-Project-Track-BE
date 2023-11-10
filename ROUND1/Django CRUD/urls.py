from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index), # 기본 화면
    path('posts/',views.post_list,name='post-list'), # 화면 보기
    # path('posts/new',views.post_create), # create
    path('posts/<int:post_id>/',views.post_detail, name='post-detail'), # read
    # path('posts/<int:post_id>/edit',views.post_update), # update
    # path('posts/<int:post_id>/delete',views.post_delete), # delete
]