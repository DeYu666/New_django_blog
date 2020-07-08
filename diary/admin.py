from django.contrib import admin
from .models import Diary
from mdeditor.widgets import MDEditorWidget
from django.db import models
# Register your models here.



class DiaryAdmin(admin.ModelAdmin):
    list_display = ['body', 'created_time','author']
    fields = ['body']

    formfield_overrides = {
	        models.TextField: {'widget': MDEditorWidget}
	}



    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    
 
# 把新增的 Postadmin 也注册进来
admin.site.register(Diary, DiaryAdmin)
