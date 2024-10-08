from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin): #NEW
    list_display = (
        "title",
        "author",
        "body",
    )
admin.site.register(Post, PostAdmin) #NEW

