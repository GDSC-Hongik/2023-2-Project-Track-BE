from django.urls import path
from . import views
urlpatterns = [
    path('',views.IndexRedirectView.as_view(),name='index'), # 기본 화면
    path('posts/',views.PostListView.as_view(),name='post-list'), # 화면 보기
    path('posts/new',views.PostCreateView.as_view(), name='post-create'), # create
    path('posts/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'), # read
    path('posts/<int:pk>/edit',views.PostUpdateView.as_view(),name='post-update'), # update
    path('posts/<int:pk>/delete',views.PostDeleteView.as_view(),name='post-delete'), # delete
]