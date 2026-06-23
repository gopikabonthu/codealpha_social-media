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

from django.urls import re_path
from django.views.static import serve

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
