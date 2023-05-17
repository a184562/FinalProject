from django.urls import path
from . import views



urlpatterns = [
     path('community/free/', views.article_list),
     path('community/free/create/', views.article_create),
     path('community/free/<int:article_pk>/',views.article_detail),

     path('community/moviereview/', views.moviereview_list),
     path('community/free/create/', views.moviereview_create),
     path('community/moviereview/<int:movie_pk>/',views.moviereview_detail),
     
]