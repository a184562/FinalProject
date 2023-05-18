from django.urls import path
from . import views



urlpatterns = [
    path('community/free/', views.article_list),
    path('community/free/<int:article_pk>/', views.article_detail),
    path('community/review/', views.Review_list),
    path('community/review/<int:review_pk>/', views.Review_detail),

]