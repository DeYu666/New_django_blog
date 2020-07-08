from django.contrib import admin
from .models import Post, Category, Tag, General_cate, Carousel
from mdeditor.widgets import MDEditorWidget
from django.db import models
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags', 'cover_url', 'title_url']

    formfield_overrides = {
	        models.TextField: {'widget': MDEditorWidget}
	}



    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    
 
# 把新增的 Postadmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(General_cate)
admin.site.register(Carousel)