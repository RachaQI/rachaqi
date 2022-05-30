from django.contrib import admin

# Register your models here.
from blogga.models import PostGa, AnswerGa


@admin.register(PostGa)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AnswerGa)
class AnswerGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'created')
