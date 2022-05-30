from django.contrib import admin


# Register your models here.
from blogiot.models import PostIot, AnswerIot


@admin.register(PostIot)
class PostIotAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AnswerIot)
class AnswerIotAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'created')
