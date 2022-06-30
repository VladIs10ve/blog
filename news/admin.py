from django.contrib import admin
from .models import Post


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, UserAdmin)
