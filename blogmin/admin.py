from django.contrib import admin

# Register your models here.
from blogmin.models import PostMin, AnswerMin


@admin.register(PostMin)
class PostMinAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(AnswerMin)
class AnswerMinAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'created')
