from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('directory/', views.users_directory_view, name='users_directory'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='user_profile'),
    path('followers/<str:username>/', views.followers_list_view, name='followers_list'),
    path('following/<str:username>/', views.following_list_view, name='following_list'),
    path('search/', views.user_search_view, name='user_search'),
]
