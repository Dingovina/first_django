import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)


class Category(models.Model):
    caterogy_name = models.CharField(max_length=60, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(choices=(
        ('News', 'news'),
        ('Article', 'article'),
    ), max_length=10)
    category = models.ManyToManyField(Category, through="PostCategory")
    create_time = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.FloatField(default=0.0)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    text = models.TextField()
    creating_time = models.DateTimeField(auto_now_add=True)


