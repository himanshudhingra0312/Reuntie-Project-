from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .manager import UserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.rue

class User(AbstractBaseUser,PermissionsMixin):

    # username=models.CharField(max_length=20,unique=True,primary_key=True)
    email=models.EmailField(verbose_name='email',max_length=60,unique=True)
    # password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    status=models.CharField(max_length=10,null=True,blank=True)
    friend=models.ManyToManyField("self")
    created_at=models.DateTimeField(auto_now_add=True)
    # is_active=models.BooleanField(default=False,blank=True,null=True)
    objects=UserManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

class Image(models.Model):
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)


class Post(models.Model):

    body=models.TextField(null=True,blank=True)
    image=models.ManyToManyField(Image,blank=True,related_name="post_image")
    user=models.ForeignKey('User', on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    
    post=models.ForeignKey("Post",on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=100)
    user=models.ForeignKey("User",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Likes(models.Model):

    post=models.ForeignKey("Post",on_delete=models.CASCADE)
    user=models.ForeignKey("User",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Notification(models.Model):

    from_user=models.ForeignKey("User", on_delete=models.CASCADE,related_name="from_user")  
    username=models.ForeignKey("User", on_delete=models.CASCADE,related_name="username")
    created_at=models.DateTimeField(auto_now_add=True)

























