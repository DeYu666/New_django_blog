from django import template
from ..models import Post, Category, Tag,General_cate,Carousel
from comments.models import Comment

register = template.Library()




@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }





@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }





@register.inclusion_tag('blog/inclusions/_general_cate.html', takes_context=True)
def show_General_cate(context, currentCate):
    dict_cate = {}
    general_cates = General_cate.objects.exclude(name='其他')
    
    for g_cate in general_cates:
        cates = Category.objects.filter(general_cate=g_cate)
        dict_cate[g_cate] = cates

    return {
        'dict_cate': dict_cate,
        'whatCate': currentCate,
    }



@register.inclusion_tag('blog/inclusions/_most_likes.html', takes_context=True)
def show_most_likes(context):
    return {
        'post_list': Post.objects.all().order_by('-likes')[:3],
    }





@register.inclusion_tag('blog/inclusions/_most_time_comments.html', takes_context=True)
def show_most_time_comments(context):
    comments = Comment.objects.all().order_by('-created_time')[:10]
    post_list = []

    for comment in comments:
        post_list.append(comment.post)

    return {
        'post_list': list(set(post_list))[:3],
    }



@register.inclusion_tag('blog/inclusions/_carousel.html', takes_context=True)
def show_carousel(context):
    carousels = Carousel.objects.all()
    post_list = []

    for carousel in carousels:
        post_list.append(carousel.post)

    return {
        'post_list': post_list[:3],
    }

    