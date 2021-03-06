from django.urls import path
from .views import *
from . import views

app_name = "main"
urlpatterns = [
  
    path('', showmain, name="showmain"),
    path('fist/', first, name="first"),
    path('second/', second, name="second"),
    path('photo1/', photo1, name="photo1"),
    path('photo2/', photo2, name="photo2"),
    path('photo3/', photo3, name="photo3"),
    path('photo4/', photo4, name="photo4"),
    path('photo5/', photo5, name="photo5"),
    path('photo5/', visit, name="visit"),
    
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),

    path('<str:post_id>/create_comment', create_comment, name="create_comment"),

    path('<str:comment_id>/update_comment', update_comment, name="update_comment" ),
    path('<str:comment_id>/delete_comment', delete_comment, name="delete_comment" ),

    # 1. like_toggle url 연결하기
    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
    path('dislike_toggle/<int:post_id>/', dislike_toggle,name="dislike_toggle"),
] 