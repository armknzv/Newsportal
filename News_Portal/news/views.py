from django.shortcuts import render, get_object_or_404
from .models import Post

"""
get_object_or_404 - используется для получения объекта из базы данных по заданным условиям. 
Если объект не найден, то функция вызывает исключение `Http404`, и возвращает страницу с ошибкой 404.
"""


def Start_Padge(request):
    news = Post.objects.filter(type='NW').order_by('-creationDate')
    return render(request, 'news/Start.html', {'news': news})


def news_list(request):
    news = Post.objects.filter(type='NW').order_by('-creationDate')  # Фильтруем только новости
    # и сортируем по убыванию даты
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'news/news_detail.html', {'post': post})
