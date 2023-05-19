from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie
from .serializers import MovieDetailSerializer,MovieListSerializer
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
    return Response(movie)
        # movie_dict = {
        #     "pk" : obj['movie_id'],
        #     "model" : "Movie.movie",
        #     "fields":{
        #         "title":obj['title'],
        #         "original_title":obj['original_title'],
        #         "poster_path": obj['poster_path'],
        #         "overview": obj['overview'],
        #         "vote_average": obj['vote_average'],
        #         "release_date": obj['release_date'],
        #         "popularity": obj['popularity'],
        #         "genres": obj['genres'],
        #     }
        # }

