from django.shortcuts import render
from .models import Post
from blog.forms import CommentForm

def index(request):
	post_list=Post.objects.all()
	return render(request, 'blog/index.html', {'post_list':post_list,})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post,})

def comment_new(request, pk):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.object.get(pk=pk)
			comment.save()
			return redirect('blog:post_detail', pk)
	else:
		form = CommentForm()
	return render(request, 'blog/comment_form.html', {'form':form,})