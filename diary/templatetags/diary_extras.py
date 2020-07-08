from django import template
from ..models import Diary




register = template.Library()




@register.inclusion_tag('diary/inclusions/_diarys.html', takes_context=True)
def show_diarys(context):
    return {
        'diary_list': Diary.objects.all()[:5],
    }


