from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
    posts = Post.objects.all().filter(status = 'PB')
    context = {
        'posts': posts,
    }
    return render(request, template_name='blog/blog.html', context=context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status='PB')
    return render(request, 'blog/post.html', context={'post': post})
