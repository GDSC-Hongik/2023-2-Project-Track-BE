from rest_framework import serializers
from .models import Movie

# 파이썬 객체의 데이터를 json 형태로 변환해주는 직렬화 실행
# 반드시 모델에서의 필드 이름과 같아야 한다.
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # 필드 조회에만 사용
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()
    
    # validated_data는 유효성 검사를 마친 데이터
    def create(self, validated_data):
        ## **은 언패킹을 의미함.
        return Movie.objects.create(**validated_data)

    # instance는 수정할 데이터
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.opening_date = validated_data.get('opening_date',instance.opening_date)
        instance.running_time = validated_data.get('running_time',instance.running_time)
        instance.overview = validated_data.get('overview',instance.overview)
        instance.save()
        return instance