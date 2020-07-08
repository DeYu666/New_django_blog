from django.shortcuts import render
from pure_pagination.mixins import PaginationMixin
from .models import Diary
from django.views.generic import ListView
import markdown #导入markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.



class DiaryAllView(PaginationMixin,ListView):
    model = Diary
    template_name = 'blog/diary.html'
    context_object_name = 'diary_list'
    paginate_by = 20
 

    def get_object(self, queryset=None):
        diary = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ])
        diary.body = md.convert(diary.body)
        return diary
