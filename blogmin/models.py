from django.contrib.auth.models import User
from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class PostMin(models.Model):
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
        return reverse('blogmin:detail-min', kwargs={'slug': self.slug})


# # SIGNALS => Transforma o Título em Slug e salva no banco para exibir nas páginas!

def pre_save_min(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.title)


signals.pre_save.connect(pre_save_min, sender=PostMin)


class AnswerMin(models.Model):
    title = models.ForeignKey(PostMin, on_delete=models.CASCADE, related_name='answersmin', verbose_name='Dúvida')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    body = models.TextField(verbose_name='Resposta')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Resposta {} de {}'.format(self.body, self.author)
