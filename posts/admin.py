from django.contrib import admin
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_filter = ('is_published',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'post', 'created_at')
    list_filter = ('created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)