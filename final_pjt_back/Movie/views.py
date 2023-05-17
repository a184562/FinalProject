from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie
from .serializers import MovieDetailSerializer,MovieListSerializer



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