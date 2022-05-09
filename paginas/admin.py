from django.contrib import admin

from .models import PostGa, PostIot, PostMin


# Register your models here.

@admin.register(PostGa)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PostIot)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(PostMin)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
