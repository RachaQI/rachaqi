from django.contrib import admin

from .models import PostGa, PostIot, PostMin

# Register your models here.

admin.site.register(PostGa)
admin.site.register(PostIot)
admin.site.register(PostMin)
