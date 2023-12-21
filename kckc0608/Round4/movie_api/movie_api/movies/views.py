from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializer import MovieSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True) # 여러 데이터 리스트를 직렬화 하는 경우
    return Response(serializer.data, status=200)