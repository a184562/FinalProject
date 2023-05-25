from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Genre


# 팔로우한 유저의 정보를 알기 위한 serializer
class UserSerializer(serializers.ModelSerializer):
    class FollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)
    followers = FollowSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'

# 유저가 선호하는 장르를 파악하기 위한 serializer
class UserGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 유저 선호 장르와 연결해주기 위한 serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'