from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie
from .serializers import MovieDetailSerializer,MovieListSerializer
import json

@api_view(['GET','POST'])
def movie_list(request):
    if request.method=='GET':
        movie = get_list_or_404(Movie)
        serializer = MovieListSerializer(movie,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        movie = Movie(id=request.data['pk'], 
        title = request.data['fields']['title'],
        original_title = request.data['fields']['original_title'],
        poster_path = request.data['fields']['poster_path'],
        overview = request.data['fields']['overview'],
        vote_average = request.data['fields']['vote_average'],
        release_date = request.data['fields']['release_date'],
        popularity = request.data['fields']['popularity'],
        )
        
        movie.save()
        for genre in request.data['fields']['genres']:
            movie.genres.add(genre)
        movie.save()
        # print('============================================================')
        # print(request.data["fields"]["genres"])
        # print('============================================================')
        return Response(movie)
        # serializer = MovieDetailSerializer(movie)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        # return Response(serializer.data)
        # return Response(movie)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

