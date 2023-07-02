from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from rest_framework.exceptions import PermissionDenied

"""creating app"""
class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReadUserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUserAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUserAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreatePostAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ReadPostAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.annotate(likes_count=Count('like'))
    serializer_class = PostSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        post = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return post


class UpdatePostAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    
    def perform_update(self, serializer):
        post = serializer.instance
        if post.owner == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to update this post.")

class DeletePostAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_destroy(self, instance):
        post = instance
        if post.owner == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this post.")

class CreateLikeAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ReadLikeAPIView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class UpdateLikeAPIView(generics.UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        like = serializer.instance
        if like.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to update this like.")

class DeleteLikeAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_destroy(self, instance):
        like = instance
        if like.user == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this like.")
