from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article,Comment,Review,ReviewComment
from .serializers import ArticleListSerializer,ArticleDetailSerializer,CommentSerializer,ReviewListSerializer,ReviewCommentSerializer,ReviewDetailSerializer


 # 기사
@api_view(['GET','POST'])
def article_list(request):
    if request.method=="GET":
      article = get_list_or_404(Article)
      serializer = ArticleListSerializer(article, many=True)
      return Response(serializer.data)
    
    elif request.method=='POST':
       serializer = ArticleDetailSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
       

@api_view(['GET','PUT','DELETE'])
def article_detail(request, article_pk):
   article = get_object_or_404(Article, pk=article_pk)
   if request.method=="GET":
      serializer = ArticleDetailSerializer(article)
      return Response(serializer.data)
   
   elif request.method=='PUT':
      serializer = ArticleDetailSerializer(article,data=request.data)
      if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
   elif request.method == 'DELETE':
      article.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      
# 댓글
@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    
@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



#영화 리뷰
@api_view(['GET','POST'])
def Review_list(request):
    if request.method=="GET":
      review = get_list_or_404(Review)
      serializer = ReviewListSerializer(review, many=True)
      return Response(serializer.data)
    
    elif request.method=='POST':
       serializer = ReviewDetailSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
       

@api_view(['GET','PUT','DELETE'])
def Review_detail(request, review_pk):
   review = get_object_or_404(Review, pk=review_pk)
   if request.method=="GET":
      serializer = ReviewDetailSerializer(review)
      return Response(serializer.data)
   
   elif request.method=='PUT':
      serializer = ReviewDetailSerializer(review,data=request.data)
      if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
      
   elif request.method == 'DELETE':
      review.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
   

# 영화 리뷰 댓글
@api_view(['GET'])
def reviewcomment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        reviewcomment = get_list_or_404(ReviewComment)
        serializer = CommentSerializer(reviewcomment, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def reviewcomment_detail(request, reviewcomment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    reviewcomment = get_object_or_404(ReviewComment, pk=reviewcomment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(reviewcomment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        reviewcomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(reviewcomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def reviewcomment_create(request, review_pk):
    # article = Article.objects.get(pk=article_pk)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
