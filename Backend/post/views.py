from django.shortcuts import render, redirect, get_object_or_404
from .models import Post 
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
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
    return render(request, 'post/index_john.html', context)
    # return render(request, 'post/content-page.html', context)


# create a post
def createPost(request):
    if request.user.is_authenticated:
        form = PostForm
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            
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
    
    comments = post.comments.filter(status = True)
    user_comment = None
    commentForm = CommentForm()
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            user_comment = commentForm.save(commit =False)
            user_comment.post = post
            user_comment.save()
    
            return redirect('post:post_detail', post.slug)
        else:
            commentForm = CommentForm()
    context = {
        'post': post,
        'commentForm': commentForm,
        'user_comments': user_comment,
        'comments': comments
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
        form = PostForm(request.POST,request.FILES, instance = post)
        if form.is_valid():
            myform = form.save(commit =False)
            myform.author = request.user
            myform.save()
            form.save_m2m()
            return redirect('post:post_detail', post.slug)
    context = {'form':form}
    return render(request, 'post/update.html', context)


class CategoryListView(ListView):
    template_name = 'post/category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        content = {
            'categories': self.kwargs['category'],
            'posts': Post.objects.filter(category__name = self.kwargs['category']).filter(status='published')
        }
        return content 


@ login_required
def bookmarks(request):
    # new = Post.objects.filter(bookmarks=request.user)
    return render(request,
                  'post/bookmarks.html',
                  {})

def contents(request):
    posts = Post.objects.filter(author = request.user).order_by('-publish_on')
    common_tags = Post.tags.most_common()[:4]

    context = {
        'posts': posts,
        'common_tags': common_tags
    }
    
    return render(request, 'post/content-page.html', context)


   
