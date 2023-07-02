"""
URL configuration for cms_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cms_app.views import (
    CreateUserAPIView, ReadUserAPIView, UpdateUserAPIView, DeleteUserAPIView,
    CreatePostAPIView, ReadPostAPIView, UpdatePostAPIView, DeletePostAPIView,
    CreateLikeAPIView, ReadLikeAPIView, UpdateLikeAPIView, DeleteLikeAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/create/', CreateUserAPIView.as_view(), name='create_user'),
    path('api/users/<int:pk>/', ReadUserAPIView.as_view(), name='read_user'),
    path('api/users/<int:pk>/update/', UpdateUserAPIView.as_view(), name='update_user'),
    path('api/users/<int:pk>/delete/', DeleteUserAPIView.as_view(), name='delete_user'),

    path('api/posts/create/', CreatePostAPIView.as_view(), name='create_post'),
    path('api/posts/<int:pk>/', ReadPostAPIView.as_view(), name='read_post'),
    path('api/posts/<int:pk>/update/', UpdatePostAPIView.as_view(), name='update_post'),
    path('api/posts/<int:pk>/delete/', DeletePostAPIView.as_view(), name='delete_post'),

    path('api/likes/create/', CreateLikeAPIView.as_view(), name='create_like'),
    path('api/likes/<int:pk>/', ReadLikeAPIView.as_view(), name='read_like'),
    path('api/likes/<int:pk>/update/', UpdateLikeAPIView.as_view(), name='update_like'),
    path('api/likes/<int:pk>/delete/', DeleteLikeAPIView.as_view(), name='delete_like'),
]

