from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile_view(request, username=None):
    if username:
        profile_user = get_object_or_404(User.objects.select_related('userprofile'), username=username)
    else:
        profile_user = request.user
        
    user_posts = profile_user.posts.select_related('author', 'author__userprofile').prefetch_related('comments', 'likes').all()
    liked_post_ids = request.user.likes.values_list('post_id', flat=True) if request.user.is_authenticated else []
    
    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = request.user.following.filter(following=profile_user).exists()
        
    context = {
        'profile_user': profile_user,
        'posts': user_posts,
        'liked_post_ids': liked_post_ids,
        'is_following': is_following,
    }
    return render(request, 'users/profile.html', context)

@login_required
def followers_list_view(request, username):
    profile_user = get_object_or_404(User.objects.select_related('userprofile'), username=username)
    followers_relations = profile_user.followers.select_related('follower', 'follower__userprofile').all()
    users_list = [rel.follower for rel in followers_relations]
    
    following_ids = request.user.following.values_list('following_id', flat=True)
    
    context = {
        'profile_user': profile_user,
        'users_list': users_list,
        'following_ids': following_ids,
        'list_type': 'Followers'
    }
    return render(request, 'users/user_list.html', context)

@login_required
def following_list_view(request, username):
    profile_user = get_object_or_404(User.objects.select_related('userprofile'), username=username)
    following_relations = profile_user.following.select_related('following', 'following__userprofile').all()
    users_list = [rel.following for rel in following_relations]
    
    following_ids = request.user.following.values_list('following_id', flat=True)
    
    context = {
        'profile_user': profile_user,
        'users_list': users_list,
        'following_ids': following_ids,
        'list_type': 'Following'
    }
    return render(request, 'users/user_list.html', context)

@login_required
def users_directory_view(request):
    users_list = User.objects.select_related('userprofile').exclude(id=request.user.id).all()
    following_ids = request.user.following.values_list('following_id', flat=True)
    
    context = {
        'users_list': users_list,
        'following_ids': following_ids,
    }
    return render(request, 'users/directory.html', context)

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)

@login_required
def user_search_view(request):
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(username__icontains=query).select_related('userprofile')
    else:
        users = User.objects.none()
    
    following_ids = request.user.following.values_list('following_id', flat=True) if request.user.is_authenticated else []
    
    context = {
        'users': users,
        'query': query,
        'following_ids': following_ids,
    }
    return render(request, 'users/search_results.html', context)
