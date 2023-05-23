from django.urls import path
from . import views


urlpatterns = [
    path('follow/<int:me_pk>/<int:user_pk>/', views.follow),
    path('followcheck/<int:me_pk>/<int:user_pk>/', views.follow_check),
    path('usergenre/',views.user_genre),
]
