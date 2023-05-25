from rest_framework import serializers
from .models import Movie,Genre,Comment
from django.contrib.auth import get_user_model

# 영화 리스트 정보
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 한줄평 정보
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)

# 영화 디테일 정보
class MovieDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields =('user_likes',)

# 장르 정보
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields ='__all__'

# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields ='__all__'