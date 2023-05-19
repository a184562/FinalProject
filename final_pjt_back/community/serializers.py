from rest_framework import serializers
from .models import Article, Comment, Review,ReviewComment




class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article')


class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','title','content','movie_title')


class ReviewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        fields = '__all__'
        # read_only_fields = ('article')


class ReviewDetailSerializer(serializers.ModelSerializer):
    comment_set = ReviewCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'