from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, MovieComment
from .serializers import MovieDetailSerializer,MovieListSerializer,MovieCommentSerializer



@api_view(['GET'])
def movie_list(request):
    movie = get_list_or_404(Movie)
    serializer = MovieListSerializer(movie,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET','POST'])
def moviecomment_list(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        moviecomment =  movie.comment_set.all()
        serializer = MovieCommentSerializer(moviecomment, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieComment(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['PUT','DELETE'])
def moviecomment_delete_update(request,movie_pk,moviecomment_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
      moviecomment = movie.comment_set.get(pk=moviecomment_pk)

      if request.method=='PUT':
            serializer = MovieCommentSerializer(moviecomment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save(user = request.user)
                  return Response(serializer.data)
      
      elif request.method=='DELETE':
            moviecomment.delete()
            return Response({'id':moviecomment_pk})

@api_view(['POST'])
def movie_like(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    
    else:
        movie.like_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
        

