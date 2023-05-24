from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie,Comment, Genre
from .serializers import MovieDetailSerializer,MovieListSerializer,CommentSerializer,GenreSerializer,UserSerializer
from .api import ans




@api_view(['GET'])
def movie_list(request):
    if request.method=='GET':
        movie = get_list_or_404(Movie)
        serializer = MovieListSerializer(movie,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def movie_data(request):
    movies = []
    for objs in ans:
        for obj in objs:
        # print(obj)
            if obj['id']==730629:
                pass
            else:
                movie = Movie(id=obj['id'], 
                title = obj['title'],
                original_title = obj['original_title'],
                poster_path = obj['poster_path'],
                overview = obj['overview'],
                vote_average = obj['vote_average'],
                release_date = obj['release_date'],
                popularity = obj['popularity'],
                )
                movie.save()
                
                for genre in obj['genre_ids']:
                    movie.genres.add(genre)
                movie.save()
                movies.append(movie)
    serializer = MovieListSerializer(movies, many=True)
    
    
    return Response(serializer.data)

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
        print(comment)
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
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    print(request.user)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def like_movie(request, movie_pk, my_pk):
    if request.method=='GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_object_or_404(get_user_model(), pk = my_pk)
        if movie.like_users.filter(pk=my_pk).exists():
            like = True
        else:
            like = False
        return Response(like)
    if request.method=='POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_object_or_404(get_user_model(), pk = my_pk)
        if movie.like_users.filter(pk=my_pk).exists():
            movie.like_users.remove(my_pk)
            like = False
        
        else:
            movie.like_users.add(my_pk)
            like = True

        return Response(like)

@api_view(['GET'])
def genres(request):
    genre = get_list_or_404(Genre)
    serializer = GenreSerializer(genre, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request,user_pk):
    user = get_object_or_404(get_user_model(),pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)