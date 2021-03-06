# Generated by Django 2.2.3 on 2020-05-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
        migrations.AddField(
            model_name='post',
            name='cover_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='封面图片的地址'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='标题图片的地址'),
        ),
    ]
