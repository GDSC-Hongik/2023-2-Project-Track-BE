from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET','POST'])
def movie_list(request):
    # /movies 접속시 자동으로 GET 요청 발송
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True) # 여러 데이터->파이썬 딕셔너리
        return Response(serializer.data,status=200) # 파이션 딕셔너리->json 파일
    elif request.method == 'POST':
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 특정 데이터 조회, 수정, 삭제를 위한 뷰
@api_view(['GET','PATCH','DELETE'])
def movie_detail(request, pk):
    # 모든 동작에서 사용하는 movie
    movie = get_object_or_404(Movie,pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = MovieSerializer(movie, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)