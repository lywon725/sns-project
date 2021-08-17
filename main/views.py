from django.contrib import admin
from .models import Dislike, Like, Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms import Form
from django.contrib.auth.decorators import login_required


# 2. 사용할 모듈 불러오기
# 2-1 POST 형식의 HTTP 통신만 받기
from django.views.decorators.http import require_POST
# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답
from django.http import HttpResponse
# 2-3 딕셔너리를 json 형식으로 바꾸기 위해
import json

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
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments})

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

def create_comment(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=post_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		Comment.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('main:detail', post_id)

# #댓글 수정하기
# def update_comment(request, com_id, post_id):
#     my_com = Comment.objects.get(id=com_id)
#     com_form = CommentForm(istance=my_com)
#     if request.method == "POST":
#         update_form = CommentForm(request.POST, instance = my_com)
#         if update_form.is_vaild():
#             update_form.save()
#             return redirect('detail', post_id)
#     return render(request, 'main/detail.html', {'com_form':com_form})

def update_comment(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        post_id = comment.post.id
        comment.content=request.POST.get('content')
        comment.save()
        return redirect('main:detail',post_id)
    return render(request, 'main/update_comment.html',{"comment":comment})

#댓글 삭제하기
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    #delete_comment = Comment.objects.get(id=comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect('main:detail', post_id)

# 3. like_toggle 함수 작성하기

@login_required
@require_POST

def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    
    context = {
        "like_count":post.like_count,
        "result":result
    }

    return HttpResponse(json.dumps(context), content_type="application/json")

def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    
    context = {
        "dislike_count":post.dislike_count,
        "result":result
    }
    return HttpResponse(json.dumps(context), content_type="application/json")