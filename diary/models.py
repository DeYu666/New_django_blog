from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User

# Create your models here.



class Diary(models.Model):
    body = MDTextField()
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)


    class Meta:
        verbose_name = '日记'
        verbose_name_plural = verbose_name