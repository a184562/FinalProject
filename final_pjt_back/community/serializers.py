from rest_framework import serializers
from .models import Article, Comment, Review,ReviewComment
from django.contrib.auth import get_user_model


# 게시글 리스트 정보 
class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = ('id','title','content','username')
        read_only_fields = ('user',)

#  게시글 댓글 정보
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)

# 게시글 디테일 정보
class ArticleDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','like_users',)

# 리뷰 게시글 리스트 정보
class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = ('id','title','content','movie_title','username')
        read_only_fields = ('user',)

# 리뷰 게시글 댓글 정보
class ReviewCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('user',)

# 리뷰 게시글 디테일 정보
class ReviewDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    reviewcomment_set = ReviewCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user','like_users',)

# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id',)
    reviews = ReviewSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = '__all__'    

