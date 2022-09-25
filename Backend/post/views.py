from django.shortcuts import render, redirect, get_object_or_404
from .models import Post 
from .forms import PostForm
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

    
def createPost(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form = 
            form.save()
            # form.author = request.user
            
            # return redirect('post:index')
        else: 
            form = PostForm
    
    context = {'form': form}

    return render(request, 'post/create.html', context)

def display_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status = 'published')
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)

