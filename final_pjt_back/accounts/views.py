from django.shortcuts import render,get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User,Genre
from .serializers import UserGenreSerializer,UserSerializer,GenreSerializer
from .api import gen
# 팔로우 기능/ 팔로워나 팔로우 갯수 확인할려면, 요청으로 갯수 가져오기
@api_view(['POST'])
def follow(request, me_pk, user_pk):
    person = get_object_or_404(User, pk=user_pk)
    me = get_object_or_404(User, pk=me_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
            me.followings.remove(person)
            following = False
        else:
            me.followings.add(person)
            following = True
        return Response(following)
    
# 팔로우 체크 확인(랜더링 되었을 때)
@api_view(['POST'])
def follow_check(request, me_pk, user_pk):
    person = get_object_or_404(User, pk = user_pk)
    me = get_object_or_404(User, pk = me_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
            following = True
        
        else:
            following = False

        return Response(following)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_genre(request):
    genres = request.data['genre']
 
    user = User(id=request.user.id,
                password=request.user.password,
                )
    for genre in genres:
        user.genres.add(genre)
    print(user.genres)

    serializer = UserGenreSerializer(user)
    return Response(serializer.data)
    # users = User(request.user)
    # if request.method == 'POST':
    #     serializer = UserGenreSerializer(users,data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user=request.user, genres=request.user.genres)
    #         return Response(serializer.data)
    # print(request.data['genre'])
    # for genre in request.data['genre']:
    #     print(genre)
    #     users.genres.add(genre)
    # serializer = UserGenreSerializer(users, many=True)
    # return Response(serializer.data)


@api_view(['GET'])
def get_user(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)



@api_view(['POST'])
def genres(request):
    genres = []
    for i in gen:
        genre=Genre(id = i['id'],
                    name=i['name'])
        genres.append(genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
