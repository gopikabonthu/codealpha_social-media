from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:pk>/edit/', views.comment_update_view, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete_view, name='comment_delete'),
    path('post/<int:pk>/like/', views.post_like_toggle_view, name='post_like_toggle'),
    path('user/<str:username>/follow/', views.user_follow_toggle_view, name='user_follow_toggle'),
]
