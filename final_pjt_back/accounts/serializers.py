from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Genre



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserGenreSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = "__all__"
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'