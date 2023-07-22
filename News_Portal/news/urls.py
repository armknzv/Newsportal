from django.urls import path
from . import views
from .views import NewsList, NewsDetail

app_name = 'news'

urlpatterns = [
    path('', views.Start_Padge, name='Start'),  # URL-шаблон Стартовой страницы
#    path('search/', NewsSearchView.as_view(), name='search'),  # URL-шаблон Поисковой страницы
    path('news/', NewsList.as_view(), name='news_list'),  # URL-шаблон для списка новостей
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('article/', views.article_list, name='article_list'),  # URL-шаблон для списка статей
    path('<int:post_id>/', views.article_detail, name='article_detail')
]
