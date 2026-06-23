"""
URL configuration for TAG project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.feed_view, name='home'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('interactions/', include('interactions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
