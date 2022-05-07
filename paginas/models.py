from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PostGa(models.Model):
    author_ga = models.ForeignKey(User, on_delete=models.CASCADE)
    title_ga = models.CharField(max_length=255)
    slug_ga = models.SlugField(max_length=255, unique=True)
    body_ga = models.TextField()
    created_ga = models.DateTimeField(auto_now_add=True)
    updated_ga = models.DateTimeField(auto_now=True)


class PostIot(models.Model):
    author_iot = models.ForeignKey(User, on_delete=models.CASCADE)
    title_iot = models.CharField(max_length=255)
    slug_iot = models.SlugField(max_length=255, unique=True)
    body_iot = models.TextField()
    created_iot = models.DateTimeField(auto_now_add=True)
    updated_iot = models.DateTimeField(auto_now=True)


class PostMin(models.Model):
    author_min = models.ForeignKey(User, on_delete=models.CASCADE)
    title_min = models.CharField(max_length=255)
    slug_min = models.SlugField(max_length=255, unique=True)
    body_min = models.TextField()
    created_min = models.DateTimeField(auto_now_add=True)
    updated_min = models.DateTimeField(auto_now=True)
