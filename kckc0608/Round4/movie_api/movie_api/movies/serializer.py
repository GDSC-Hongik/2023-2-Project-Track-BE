from rest_framework import serializers
from .models import Movie, Review
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from rest_framework.serializers import ValidationError

class MovieSerializer(serializers.ModelSerializer):
    # movie_reviews = serializers.PrimaryKeyRelatedField(source='reviews', many=True, read_only=True)
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview', 'reviews']
        # read_only_fields = ['reviews']
        validators = [
            UniqueTogetherValidator(
                queryset=Movie.objects.all(),
                fields=['name', 'overview']
            )
        ]
    
    # overview = serializers.CharField(validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=300)])
    
    def validate_overview(self, value):
        if 10 <= len(value) <= 300:
            return value
        raise ValidationError('영화 소개는 10~300자 사이로 입력해주세요.')
    
    
    # name = serializers.CharField(validators=[UniqueValidator(
    #     queryset=Movie.objects.all(),
    #     message="이미 존재하는 영화 이름입니다.",
    # )])


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
        extra_kwargs = {
            'movie': {'read_only': True},
        }