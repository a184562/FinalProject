from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article,MovieReview,Comment,MovieComment
from .serializers import ArticleListSerializer,ArticleDetailSerializer,CommentSerializer,MovieReviewDetailSerializer,MovieReviewListSerializer,MovieCommentSerializer




# 자유게시판 리스트
@api_view(['GET'])
def article_list(request):
      article = get_list_or_404(Article)
      serializer = ArticleListSerializer(article, many=True)    
      return Response(serializer.data)

# 자유게시판 디테일
@api_view(['GET'])
def article_detail(request,article_pk):
      article = get_object_or_404(Article,pk=article_pk)
      serializer = ArticleDetailSerializer(article)
      return Response(serializer.data)

@api_view(['POST'])
def article_create(request):
      serializer= ArticleDetailSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
            # serializer.save(user=request.user)
            serializer.save()
            return Response(serializer.data)
      
@api_view(['PUT','DELETE'])
def article_update_delete(request,article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      if request.method == 'PUT':
            serializer = ArticleDetailSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save(user=request.user)
                  return Response(serializer.data)
      elif request.method =='DELETE':
            article.delete()
            return Response({'id': article_pk})

@api_view(['POST'])
def article_like(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    user = request.user

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    else:
        article.like_users.add(user)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)


# 자유게시판 디테일의 댓글
@api_view(['GET'])
def comment_list(request,article_pk):
      article = get_object_or_404(Article, pk = article_pk)
      comment = article.comment_set.all()
      serializer = CommentSerializer(comment, many=True)
      return Response(serializer.data)

@api_view(['POST'])
def comment_create(request,article_pk):
      article = get_object_or_404(Article, pk = article_pk)
      serializer = CommentSerializer(data = request.data)
      if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data)

@api_view(['PUT','DELETE'])
def comment_delete_update(request,article_pk,comment_pk):
      article = get_object_or_404(Article, pk=article_pk)
      comment = article.comment_set.get(pk=comment_pk)

      if request.method=='PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save(user = request.user)
                  return Response(serializer.data)
      
      elif request.method=='DELETE':
            comment.delete()
            return Response({'id':comment_pk})

@api_view(['POST'])
def comment_like(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    user = request.user

    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    else:
        comment.like_users.add(user)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)




# 영화 게시판 
@api_view(['GET'])
def moviereview_list(request):
      moviereview = get_list_or_404(MovieReview)
      serializer = MovieReviewListSerializer(moviereview,many=True)
      return Response(serializer.data)

@api_view(['GET'])
def moviereview_detail(request,movie_pk):
      moviereview = get_object_or_404(MovieReview, pk=movie_pk)
      serializer = MovieReviewDetailSerializer(moviereview)
      return Response(serializer.data)


@api_view(['POST'])
def moviereview_create(request):
      serializer = MovieReviewDetailSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
      

@api_view(['PUT','DELETE'])
def moviereview_delete_update(request,movie_pk):
      moviereview=get_object_or_404(MovieReview,pk=movie_pk)
      if request.method =='PUT':
            serializer = MovieReviewDetailSerializer(moviereview,data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save(user=request.user)
                  return Response(serializer.data)
      elif request.method =='DELETE':
            moviereview.delete()
            return Response({'id':movie_pk})     

@api_view(['POST'])
def moviereview_like(request,movie_pk):
    moviereview = get_object_or_404(MovieReview,pk=movie_pk)
    user = request.user

    if moviereview.like_users.filter(pk=user.pk).exists():
        moviereview.like_users.remove(user)
        serializer = MovieReviewDetailSerializer(moviereview)
        return Response(serializer.data)
    
    else:
        moviereview.like_users.add(user)
        serializer = MovieReviewDetailSerializer(moviereview)
        return Response(serializer.data)


# 영화 게시판 댓글
@api_view(['GET'])
def moviecomment_list(request,movie_pk):
      moviereview = get_object_or_404(MovieReview, pk = movie_pk)
      comment = moviereview.comment_set.all()
      serializer = MovieCommentSerializer(comment, many=True)
      return Response(serializer.data)

@api_view(['POST'])
def moviecomment_create(request,movie_pk):
      moviereview = get_object_or_404(MovieReview, pk = movie_pk)
      serializer = MovieCommentSerializer(data = request.data)
      if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, moviereview=moviereview)
            return Response(serializer.data)

@api_view(['PUT','DELETE'])
def moviecomment_delete_update(request,movie_pk,moviecomment_pk):
      moviereview = get_object_or_404(MovieReview, pk=movie_pk)
      moviecomment = moviereview.comment_set.get(pk=moviecomment_pk)

      if request.method=='PUT':
            serializer = MovieCommentSerializer(moviecomment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save(user = request.user)
                  return Response(serializer.data)
      
      elif request.method=='DELETE':
            moviecomment.delete()
            return Response({'id':moviecomment_pk})


@api_view(['POST'])
def moviecomment_like(request,comment_pk):
    moviecomment = get_object_or_404(MovieComment,pk=comment_pk)
    user = request.user

    if moviecomment.like_users.filter(pk=user.pk).exists():
        moviecomment.like_users.remove(user)
        serializer = MovieCommentSerializer(moviecomment)
        return Response(serializer.data)
    
    else:
        moviecomment.like_users.add(user)
        serializer = MovieCommentSerializer(moviecomment)
        return Response(serializer.data)

