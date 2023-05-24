from rest_framework import serializers
from .models import Movie,Genre,Comment
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)

class MovieDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields =('user_likes',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields ='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class MovieLikeSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)
    like_movies = MovieLikeSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields ='__all__'