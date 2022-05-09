# Generated by Django 4.0.4 on 2022-05-07 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postga',
            name='author_ga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='postga',
            name='body_ga',
            field=models.TextField(verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='postga',
            name='created_ga',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado'),
        ),
        migrations.AlterField(
            model_name='postga',
            name='slug_ga',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='postga',
            name='title_ga',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='postga',
            name='updated_ga',
            field=models.DateTimeField(auto_now=True, verbose_name='Editado'),
        ),
        migrations.AlterField(
            model_name='postiot',
            name='author_iot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='postiot',
            name='body_iot',
            field=models.TextField(verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='postiot',
            name='created_iot',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado'),
        ),
        migrations.AlterField(
            model_name='postiot',
            name='slug_iot',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='postiot',
            name='title_iot',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='postiot',
            name='updated_iot',
            field=models.DateTimeField(auto_now=True, verbose_name='Editado'),
        ),
        migrations.AlterField(
            model_name='postmin',
            name='author_min',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='postmin',
            name='body_min',
            field=models.TextField(verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='postmin',
            name='created_min',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado'),
        ),
        migrations.AlterField(
            model_name='postmin',
            name='slug_min',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='postmin',
            name='title_min',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='postmin',
            name='updated_min',
            field=models.DateTimeField(auto_now=True, verbose_name='Editado'),
        ),
    ]