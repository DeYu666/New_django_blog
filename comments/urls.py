from django.urls import path
 
from . import views
 
app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
    path('commentReply/<int:comment_pk>', views.commentReply, name='commentReply'),
    path('postBorad/', views.Post_borad, name='postBorad'),
    path('link/', views.Links, name='link'),
]

