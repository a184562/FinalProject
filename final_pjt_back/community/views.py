from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Article,Comment,Review,ReviewComment
from .serializers import ArticleListSerializer,ArticleDetailSerializer,CommentSerializer,ReviewListSerializer,ReviewCommentSerializer,ReviewDetailSerializer,UserSerializer
from django.contrib.auth import get_user_model
 # 기사
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method=="GET":
      article = get_list_or_404(Article)
      serializer = ArticleListSerializer(article, many=True)
      return Response(serializer.data)
    elif request.method=='POST':
       serializer = ArticleDetailSerializer(data=request.data)

       if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
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
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
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
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user,article=article)
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
          serializer.save(user=request.user)
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
        reviewcomment = get_list_or_404(ReviewComment)
        serializer = ReviewCommentSerializer(reviewcomment, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def reviewcomment_detail(request, reviewcomment_pk):
    reviewcomment = get_object_or_404(ReviewComment, pk=reviewcomment_pk)

    if request.method == 'GET':
        serializer = ReviewCommentSerializer(reviewcomment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        reviewcomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewCommentSerializer(reviewcomment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def reviewcomment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user,review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def like_article(request, article_pk, my_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = get_object_or_404(get_user_model(), pk = my_pk)
    if request.method =='GET':
        if article.like_users.filter(pk=my_pk).exists():
            like = True
        else:
            like = False
        return Response(like)

    elif request.method =='POST':
        if article.like_users.filter(pk=my_pk).exists():
            article.like_users.remove(my_pk)
            like = False
        
        else:
            article.like_users.add(my_pk)
            like = True

        return Response(like)


@api_view(['GET','POST'])
def like_review(request, review_pk, my_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = get_object_or_404(get_user_model(), pk = my_pk)
    if request.method =='GET':
        if review.like_users.filter(pk=my_pk).exists():
            like = True
        else:
            like = False
        return Response(like)

    elif request.method =='POST':
        if review.like_users.filter(pk=my_pk).exists():
            review.like_users.remove(my_pk)
            like = False
        
        else:
            review.like_users.add(my_pk)
            like = True

        return Response(like)
    

# @api_view(['GET'])
# def get_user(request,user_pk):
#     user = get_object_or_404(get_user_model(),pk=user_pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)
