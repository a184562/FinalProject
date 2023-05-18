from rest_framework import serializers
from .models import Article,Comment,MovieReview,MovieComment

# 자유게시판 LIST
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title')
        # read_only_fields = ('user')
      
# 자유게시판 DETAIL
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)

# 영화리뷰게시판 LIST
class MovieReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ('title','movie_title','rank','user','like_users')
        read_only_fields = ('user',)

# 영화리뷰게시판 DETAIL
class MovieReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ('user',)

# 댓글 기능
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','article')

class MovieCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('user','article')
