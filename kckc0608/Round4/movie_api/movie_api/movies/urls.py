from django.urls import path
from .views import movie_list, movie_detail, review_list, MovieList, MovieDetail

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('movies/<int:pk>/reviews', review_list),
]
