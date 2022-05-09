from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class PostGa(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body = models.TextField(verbose_name="Texto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    def __str__(self):
        return "{} ({})".format(self.author, self.title)


class PostIot(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body = models.TextField(verbose_name="Texto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    def __str__(self):
        return "{} ({})".format(self.author, self.title)


class PostMin(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body = models.TextField(verbose_name="Texto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    def __str__(self):
        return "{} ({})".format(self.author, self.title)
