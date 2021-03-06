from django.contrib.auth.models import User
from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.

class PostGa(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Link")
    body = models.TextField(verbose_name="Texto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} ({})".format(self.author, self.title)

    def get_absolute_url(self):
        return reverse('blogga:detail-ga', kwargs={'slug': self.slug})


# SIGNALS => Transforma o Título em Slug e salva no banco para exibir nas páginas!

def pre_save_ga(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.title)


signals.pre_save.connect(pre_save_ga, sender=PostGa)


class AnswerGa(models.Model):
    title = models.ForeignKey(PostGa, on_delete=models.CASCADE, related_name='answersga', verbose_name='Dúvida')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    body = models.TextField(verbose_name='Resposta')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Resposta {} de {}'.format(self.body, self.author)
