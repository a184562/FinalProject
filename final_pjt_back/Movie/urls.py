from django.urls import path
from . import views


urlpatterns = [
    path('movies/',views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
]