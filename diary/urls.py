from django.urls import path
 
from . import views


app_name = 'diary'

urlpatterns = [
    path('diary/', views.DiaryAllView.as_view(), name='diaryAll'),
]