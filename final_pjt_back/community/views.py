from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article,MovieReview
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
            serializer.save(user=request.user)
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





