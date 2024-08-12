from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from .models import Post, Comment
from .forms import CommentForm

def blog(request):
    posts = Post.objects.all().filter(status = 'PB')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, template_name='blog/blog.html', context=context)

def post_detail(request, slug):
    post = get_object_or_404(Post, 
                             status='PB',
                             slug=slug,)
    posts = Post.objects.all().exclude(slug=slug)[:3]
    comments = Comment.objects.all().filter(post=post.id)
    form = CommentForm()
    return render(request, 'blog/post.html', context={'post': post, 
                                                      'first_posts': posts, 
                                                      'comments': comments,
                                                      'form': form,})


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='PB')
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/comment_form.html', context={'form': form, 'post': post, 'comment': comment})
    