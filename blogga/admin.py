from django.contrib import admin


# Register your models here.
from blogga.models import PostGa


@admin.register(PostGa)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
