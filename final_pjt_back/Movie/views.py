from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie,Genre
from .serializers import MovieDetailSerializer,MovieListSerializer,GenreSerializer


@api_view(['GET','POST'])
def movie_list(request):
    if request.method=='GET':
        movie = get_list_or_404(Movie)
        serializer = MovieListSerializer(movie,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        genres = []

        
        movie = Movie(id=request.data['movie_id'], 
        title = request.data['title'],
        original_title = request.data['original_title'],
        poster_path = request.data['poster_path'],
        overview = request.data['overview'],
        vote_average = request.data['vote_average'],
        release_date = request.data['release_date'],
        popularity = request.data['popularity'],
        )
        
        movie.save()
        for genre in request.data['genres']:
            movie.genres.add(genre)   
            # movie.genres        
        if movie.is_valid(raise_exeception=True):
            movie.save()
            return Response(movie)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def genre(request):
    genre = GenreSerializer(data=request.data)
    if genre.is_valid():
        genre.save()
        return Response(genre.data)