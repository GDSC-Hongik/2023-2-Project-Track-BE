from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)