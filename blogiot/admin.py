from django.contrib import admin


# Register your models here.
from blogiot.models import PostIot


@admin.register(PostIot)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
