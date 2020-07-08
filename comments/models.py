from django.db import models
from django.utils import timezone
 
 
class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]
 
    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])


class CommentReply(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    comment = models.ForeignKey('Comment', verbose_name='评论回复', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论回复'
        verbose_name_plural = verbose_name
        ordering = ["created_time"]

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])


class PostBorad(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
 
    class Meta:
        verbose_name = '留言板'
        verbose_name_plural = verbose_name
 
    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])


class Link(models.Model):
    name = models.CharField('链接名字', max_length=50)
    excerpt = models.CharField('链接摘要', max_length=200, blank=True)
    url = models.URLField('链接网址', blank=True)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
