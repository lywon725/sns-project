from django.contrib import admin
from .models import Post
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

# Create your views here.

def showmain(request):
    post = Post.objects.all()
    return render(request, 'main/mainpage.html', {'post':post})

def first(request):
    return render(request, 'main/first.html')

def second(request):
    return render(request, 'main/second.html')

def photo1(request):
    return render(request, 'main/photo_1.html')
def photo2(request):
    return render(request, 'main/photo_2.html')
def photo3(request):
    return render(request, 'main/photo_3.html')
def photo4(request):
    return render(request, 'main/photo_4.html')
def photo5(request):
    return render(request, 'main/photo_5.html')

def visit(request):
    return render(request, 'main/visited.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image') # 여기 수정
    new_post.save()
    return redirect('main:detail', new_post.id) # 여기 수정

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:showmain')