from django.contrib import admin


# Register your models here.
from blogmin.models import PostMin


@admin.register(PostMin)
class PostGaAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
