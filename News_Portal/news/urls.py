from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.Start_Padge, name='Start'),
    path('news/', views.news_list, name='news_list'),  # URL-шаблон для списка новостей
    path('<int:post_id>/', views.news_detail, name='news_detail')
]
