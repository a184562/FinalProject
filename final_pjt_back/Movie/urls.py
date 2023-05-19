from django.urls import path
from . import views


urlpatterns = [
    path('movies/',views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('moviedata/',views.movie_data),
    path('comments/', views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('movie/<int:movie_pk>/comments/', views.comment_create),

]