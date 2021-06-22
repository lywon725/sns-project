from django.urls import path
from . import views

app_name = "usrers"
urlpatterns = [
  path('mypage/', views.mypage, name="mypage"),

]