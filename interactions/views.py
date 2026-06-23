from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comment, Like, Follow
from .forms import CommentForm

@login_required
def comment_update_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "You don't have permission to edit this comment.")
        return redirect('post_detail', pk=comment.post.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated!')
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'interactions/comment_form.html', {'form': form, 'comment': comment})

@login_required
def comment_delete_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "You don't have permission to delete this comment.")
        return redirect('post_detail', pk=comment.post.id)

    if request.method == 'POST':
        post_id = comment.post.id
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
        return redirect('post_detail', pk=post_id)

    return render(request, 'interactions/comment_confirm_delete.html', {'comment': comment})

@login_required
def post_like_toggle_view(request, pk):
    if request.method == 'POST':
        from posts.models import Post
        post = get_object_or_404(Post, pk=pk)
        
        # Check if the user already liked the post
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
            # Unlike
            like_qs.delete()
        else:
            # Like
            Like.objects.create(user=request.user, post=post)
            
        # Redirect back to where they came from
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'home'))
        return redirect(next_url)
    
    return redirect('home')

@login_required
def user_follow_toggle_view(request, username):
    if request.method == 'POST':
        from django.contrib.auth.models import User
        target_user = get_object_or_404(User, username=username)
        
        if request.user == target_user:
            messages.error(request, "You cannot follow yourself.")
        else:
            follow_qs = Follow.objects.filter(follower=request.user, following=target_user)
            if follow_qs.exists():
                # Unfollow
                follow_qs.delete()
            else:
                # Follow
                Follow.objects.create(follower=request.user, following=target_user)
                
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'home'))
        return redirect(next_url)
    
    return redirect('home')
