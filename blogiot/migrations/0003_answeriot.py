# Generated by Django 4.0.4 on 2022-05-30 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogiot', '0002_alter_postiot_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerIot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Resposta')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answersiot', to='blogiot.postiot', verbose_name='Dúvida')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
