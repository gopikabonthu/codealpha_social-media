from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_update_view, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete_view, name='post_delete'),
]
