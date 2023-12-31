from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Movie,Review
from .serializers import MovieSerializer, ReviewSerializer

# view 마다 다른 pagination을 적용하고 싶다면 사용
class MoviePageNumberPagination(PageNumberPagination):
    page_size = 2

# ListCreateAPIView 에서 queryset 과 serializer_class 는 필수 조건
class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePageNumberPagination

# 특정 데이터 조회, 수정, 삭제를 위한 뷰
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        movie = get_object_or_404(Movie,pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)
    
    def perform_create(self,serializer):
        movie = get_object_or_404(Movie,pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)