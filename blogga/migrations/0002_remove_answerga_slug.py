# Generated by Django 4.0.4 on 2022-05-29 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerga',
            name='slug',
        ),
    ]
