from django import template
from ..forms import CommentForm,CommentReplyForm
 
register = template.Library()
 
 
@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }


@register.inclusion_tag('comments/inclusions/_form2.html', takes_context=True)
def show_commentReply_form(context, comment_id, form=None):
    if form is None:
        form = CommentReplyForm()
    return {
        'form': form,
        'comment_id': comment_id,
    }


@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    return {
        'comment_list': comment_list,
    }