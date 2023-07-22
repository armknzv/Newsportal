from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

"""
get_object_or_404 - используется для получения объекта из базы данных по заданным условиям. 
Если объект не найден, то функция вызывает исключение `Http404`, и возвращает страницу с ошибкой 404.
"""


def Start_Padge(request):
    news = Post.objects.filter(type='NW').order_by('-creationDate')[:4]
    return render(request, 'news/Start.html', {'news': news})


class NewsList(ListView):
    paginate_by = 10
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset().filter(type='NW')
        return queryset.order_by('-creationDate')


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'


def article_list(request):
    article = Post.objects.filter(type='AR').order_by('-creationDate')  # Фильтруем только статьи
    # и сортируем по убыванию даты
    paginator = Paginator(article, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'news/article_list.html', {'articles': articles})


def article_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'news/article_detail.html', {'post': post})
