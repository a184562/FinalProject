from rest_framework import serializers
from .models import Article, Comment, Review,ReviewComment
from django.contrib.auth import get_user_model



class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)


    class Meta:
        model = Article
        fields = ('id','title','content','username')
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','like_users',)


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ('id','title','content','movie_title','username')
        read_only_fields = ('user',)


class ReviewCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('user',)


class ReviewDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    reviewcomment_set = ReviewCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user','like_users',)


class UserSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('article',)
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('review',)
    review = ReviewSerializer(many=True, read_only=True)
    article = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = '__all__'    

