from rest_framework import serializers
from .models import Article,Comment,CommentToComment

# 자유게시판 LIST
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','user','like_users')
        read_only_fields = ('user')
      
# 자유게시판 DETAIL
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','content','created_at','updated_at','user','like_users',)
        read_only_fields = ('user',)

# 영화리뷰게시판 LIST
class MovieReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','movie_title','rank','user','like_users')
        read_only_fields = ('user',)

# 영화리뷰게시판 LIST
class MovieReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

# 댓글 기능
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','article')

# 대댓글 기능
class CommentToCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentToComment
        fields = '__all__'
        read_only_fields = ('user','comment')