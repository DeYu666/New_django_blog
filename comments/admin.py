from django.contrib import admin
from .models import Comment, PostBorad, Link, CommentReply
 
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']


class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'comment', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'comment']


admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
admin.site.register(PostBorad)
admin.site.register(Link)
