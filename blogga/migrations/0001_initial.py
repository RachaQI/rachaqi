# Generated by Django 4.0.4 on 2022-05-14 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Link')),
                ('body', models.TextField(verbose_name='Texto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
        ),
    ]
