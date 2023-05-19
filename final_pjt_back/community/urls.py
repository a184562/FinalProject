from django.urls import path
from . import views



urlpatterns = [
    path('community/free/', views.article_list),
    path('community/free/<int:article_pk>/', views.article_detail),
    path('community/free/comment/', views.comment_list),
    path('community/free/comment/<int:comment_pk>/', views.comment_detail),
    path('community/free/<int:article_pk>/comments/', views.comment_create),
    
    path('community/review/', views.Review_list),
    path('community/review/<int:review_pk>/', views.Review_detail),
    path('community/review/comment/', views.reviewcomment_list),
    path('community/review/comment/<int:reviewcomment_pk>/', views.reviewcomment_detail),
    path('community/review/<int:review_pk>/comments/', views.reviewcomment_create),

]