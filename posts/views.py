from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

from interactions.forms import CommentForm

def feed_view(request):
    filter_type = request.GET.get('filter', 'all')
    
    if filter_type == 'following' and request.user.is_authenticated:
        following_users = request.user.following.values_list('following', flat=True)
        posts = Post.objects.filter(author__in=following_users).select_related('author', 'author__userprofile').prefetch_related('comments', 'likes')
    else:
        posts = Post.objects.select_related('author', 'author__userprofile').prefetch_related('comments', 'likes').all()
    
    liked_post_ids = []
    if request.user.is_authenticated:
        liked_post_ids = request.user.likes.values_list('post_id', flat=True)

    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post was created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    
    context = {
        'posts': posts,
        'form': form,
        'liked_post_ids': liked_post_ids
    }
    return render(request, 'posts/feed.html', context)

def post_detail_view(request, pk):
    post = get_object_or_404(Post.objects.select_related('author', 'author__userprofile').prefetch_related('comments', 'likes'), pk=pk)
    comments = post.comments.select_related('author', 'author__userprofile').all()
    
    is_liked = False
    if request.user.is_authenticated:
        is_liked = post.likes.filter(user=request.user).exists()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment was added successfully!')
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'is_liked': is_liked
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user != post.author:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'posts/post_form.html', {'form': form, 'post': post})

@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('home')
        
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
