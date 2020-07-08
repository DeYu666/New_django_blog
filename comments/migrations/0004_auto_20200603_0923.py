# Generated by Django 2.2.3 on 2020-06-03 01:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名字')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('url', models.URLField(blank=True, verbose_name='网址')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Comment', verbose_name='评论回复')),
            ],
            options={
                'verbose_name': '评论回复',
                'verbose_name_plural': '评论回复',
                'ordering': ['created_time'],
            },
        ),
    ]
