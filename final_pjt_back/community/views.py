from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article,Comment
from .serializers import ArticleListSerializer,ArticleDetailSerializer,CommentSerializer



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

