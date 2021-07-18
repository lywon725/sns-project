from django.contrib import admin
from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms import Form

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