from django.shortcuts import render, redirect, get_object_or_404
from .models import Post 
# Create your views here.
def index(request):
    # retrieve all posts and order them by their publish date 
    posts = Post.objects.filter(status='published').order_by('-publish_on')
    common_tags = Post.tags.most_common()[:4]

    context = {
        'posts': posts,
        'common_tags': common_tags
    }
    return render(request, 'post/index.html', context)

def display_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status = 'published')
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)

