from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag, General_cate
import re
from django.views.generic import ListView,DetailView
import markdown #导入markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from pure_pagination.mixins import PaginationMixin
import json




class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    paginate_by = 12

    def get_queryset(self):
        cate = get_object_or_404(Category, name='其他')
        return super(IndexView,self).get_queryset().exclude(category=cate)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        cate = get_object_or_404(Category,  name='其他')

        other_post = Post.objects.filter(category=cate)[:3]

        # Add in a QuerySet of all the books
        context['otherPost'] = other_post
        return context


class BlogAllView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 12

    def get_queryset(self):
        cate = get_object_or_404(Category, name='其他')
        return super(BlogAllView, self).get_queryset().exclude(category=cate)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the books
        context['isBlog'] = 1  # 是否为 blog 的全部文章页
        return context




class CategoryView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 12

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))

        context['isBlog'] = 0  # 是否为 blog 的全部文章页
        context['whatCate'] = cate.general_cate
        context['cateName'] = cate
        return context





class TagView(PaginationMixin,ListView):
    model = Post
    template_name = 'blog/blog_tag.html'
    context_object_name = 'post_list'

    paginate_by = 12


    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))

        context['tagName'] = tag
        return context




# 记得在顶部导入 DetailView
class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
 
    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)
 
        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()
 
        # 视图必须返回一个 HttpResponse 对象
        return response
 
    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])

        post.body = md.convert(post.body)
        post.toc = md.toc
 
        return post




    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')

        post_list = Post.objects.filter(pk__in=[p for p in range(pk-2,pk+5)]).exclude(pk=pk)


        context['relatedPost'] = post_list[:4]
        return context








 
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})




def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    


    # 阅读量 +1
    post.increase_views()


    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    post.body = md.convert(post.body)
    post.toc = md.toc
    return render(request, 'blog/detail.html', context={'post': post})




def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/blog.html', context={'post_list': post_list})




def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})



def Dolike(request,pk):
    print("\n\n\n 进来了")
    post = get_object_or_404(Post, pk=pk)
    post.increase_likes()

    print("\n\n\n 进来了")
    dic = {
        "name": "alex"
    }
    data = json.dumps(dic)  # 转换为字符串
    return HttpResponse({json.dumps(data)}, content_type='application/json')

