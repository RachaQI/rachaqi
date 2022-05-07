from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class PostGa(models.Model):
    author_ga = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title_ga = models.CharField(max_length=255, verbose_name="Título")
    slug_ga = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body_ga = models.TextField(verbose_name="Texto")
    created_ga = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated_ga = models.DateTimeField(auto_now=True, verbose_name="Editado")

    def __str__(self):
        return


class PostIot(models.Model):
    author_iot = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title_iot = models.CharField(max_length=255, verbose_name="Título")
    slug_iot = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body_iot = models.TextField(verbose_name="Texto")
    created_iot = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated_iot = models.DateTimeField(auto_now=True, verbose_name="Editado")


class PostMin(models.Model):
    author_min = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title_min = models.CharField(max_length=255, verbose_name="Título")
    slug_min = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body_min = models.TextField(verbose_name="Texto")
    created_min = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated_min = models.DateTimeField(auto_now=True, verbose_name="Editado")
