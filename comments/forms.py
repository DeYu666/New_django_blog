from django import forms
from .models import Comment,CommentReply

# from django.utils.translation import ugettext_lazy as _
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows':5,'class': 'myfieldclass','placeholder':'请留言...'}),
            'name': forms.TextInput(attrs={'placeholder':'姓名','class':'comment-input'}),
            'email': forms.TextInput(attrs={'placeholder':'邮箱','class':'comment-input'}),
            'url': forms.TextInput(attrs={'placeholder':'网站','class':'comment-input'}),
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['name', 'email', 'url', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows':5,'class': 'myfieldclass','placeholder':'请留言...'}),
            'name': forms.TextInput(attrs={'placeholder':'姓名','class':'comment-input'}),
            'email': forms.TextInput(attrs={'placeholder':'邮箱','class':'comment-input'}),
            'url': forms.TextInput(attrs={'placeholder':'网站','class':'comment-input'}),
        }