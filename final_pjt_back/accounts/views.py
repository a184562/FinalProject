from django.shortcuts import render,get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User


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
