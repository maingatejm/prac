from django.shortcuts import render, redirect
from .models import Post, Comment
from blog.forms import CommentForm
from django.contrib import messages

def index(request):
	post_list=Post.objects.all()
	return render(request, 'blog/index.html', {'post_list':post_list,})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	comment_list = Comment.objects.all().filter(post=post)
	return render(request, 'blog/post_detail.html', {'post':post, 'comment_list':comment_list})

def comment_new(request, pk):
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.objects.get(pk=pk)
			comment.save()
			messages.info(request, '댓글이 등록되었습니다.')
			return redirect('blog:post_detail', pk)
	else:
		form = CommentForm()
	return render(request, 'blog/comment_form.html', {'form':form,})

