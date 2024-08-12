from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'author', 'created']
    search_fields = ['title', 'body']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
class CommentAdmine(admin.ModelAdmin):
    list_display = ['post', 'name', 'created', 'active']
    list_filter = ['name', 'active']
    ordering = ['created']