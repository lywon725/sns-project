"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name="showmain"),
    path('fist/', views.first, name="first"),
    path('second/', views.second, name="second"),
    path('photo1/', views.photo1, name="photo1"),
    path('photo2/', views.photo2, name="photo2"),
    path('photo3/', views.photo3, name="photo3"),
    path('photo4/', views.photo4, name="photo4"),
    path('photo5/', views.photo5, name="photo5"),
    path('photo5/', views.visit, name="visit"),
    path('<str:id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]
