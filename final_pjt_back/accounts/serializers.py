from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Genre



class UserSerializer(serializers.ModelSerializer):
    class FollowSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('id',)
            
    followers = FollowSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'


class UserGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'