from django.shortcuts import render

def index(request):
	return render(request, 'blog/index.html')

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post'=post,})