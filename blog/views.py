from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
    posts = Post.objects.all().filter(status = 'PB')
    context = {
        'posts': posts,
    }
    return render(request, template_name='blog/blog.html', context=context)

def post_detail(request, slug):
    post = get_object_or_404(Post, 
                             status='PB',
                             slug=slug,)
    posts = Post.objects.all().exclude(slug=slug)[:3]
    return render(request, 'blog/post.html', context={'post': post, 'first_posts': posts})
