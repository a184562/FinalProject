from rest_framework import serializers
from .models import Article, Comment, Review,ReviewComment




class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)


    class Meta:
        model = Article
        fields = ('id','title','content')


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article')


class ArticleDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = ('id','title','content','movie_title')


class ReviewCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ReviewComment
        fields = '__all__'
        # read_only_fields = ('article')


class ReviewDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = ReviewCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'