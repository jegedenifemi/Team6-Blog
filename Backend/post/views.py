from django.shortcuts import render, redirect, get_object_or_404
from .models import Post 
from .forms import PostForm
from django.contrib import messages

# Create your views here.
# list view for home page
def index(request):
    # retrieve all posts and order them by their publish date 
    posts = Post.objects.filter(status='published').order_by('-publish_on')
    common_tags = Post.tags.most_common()[:4]

    context = {
        'posts': posts,
        'common_tags': common_tags
    }
    return render(request, 'post/index.html', context)

# create a post
def createPost(request):
    if request.user.is_authenticated:
        form = PostForm
        if request.method == 'POST':
            form = PostForm(request.POST)
            
            if form.is_valid():
                myform = form.save(commit =False)
                myform.author = request.user
                myform.save()
                form.save_m2m()
                return redirect('post:index')
            else: 
                form = PostForm
    else:
        return redirect('login')
    
    context = {'form': form}

    return render(request, 'post/create.html', context)


# specific posts
def postDetail(request, slug):
    post = get_object_or_404(Post, slug=slug, status = 'published')
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)



# this is supposed to be for only bloggers but might just redo it
def bloggerDetail(request, slug):
    pass


# deleting posts
def postDelete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    blogger = post.author

    if request.method == 'POST' and request.user.is_authenticated and (request.user == blogger or request.user.is_staff):
        post.delete()
        messages.success(request, 'Post has being successfully deleted! ')
        return redirect('post:index')

    context = {
        'post':post,
        'blogger':blogger,
    }
    return render(request, 'post/delete.html', context)


# updating posts
def update(request, slug):
    post = Post.objects.get(slug = slug)
    form = PostForm(instance  = post)
    if request.method  == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            myform = form.save(commit =False)
            myform.author = request.user
            myform.save()
            form.save_m2m()
            return redirect('post:index')
    context = {'form':form}
    return render(request, 'post/update.html', context)





