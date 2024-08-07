from django.shortcuts import render
from .models import Post

def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template_name='blog/blog.html', context=context)
