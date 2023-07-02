from django.db import models
from django.contrib.auth import get_user_model



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

User = get_user_model()
   

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
  

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

