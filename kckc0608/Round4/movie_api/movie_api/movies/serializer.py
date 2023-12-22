from rest_framework import serializers
from .models import Movie
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.validators import UniqueValidator

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
    
    overview = serializers.CharField(validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=300)])
    name = serializers.CharField(validators=[UniqueValidator(
        queryset=Movie.objects.all(),
        message="이미 존재하는 영화 이름입니다.",
    )])