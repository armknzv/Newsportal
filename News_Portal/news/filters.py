import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    """
    Создаем свой набор фильтров для модели Post.
    FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
    """
    type = django_filters.CharFilter(lookup_expr='exact')  # поиск по типу
    title = django_filters.CharFilter(lookup_expr='icontains')  # поиск по названию
    author = django_filters.CharFilter(lookup_expr='icontains'),  # поиск по автору
    postCategory = django_filters.CharFilter(lookup_expr='exact')  # поиск по категории
    creationDate = django_filters.DateFilter(field_name='creationDate', lookup_expr='gte')

    class Meta:
        """
        В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        """
        model = Post
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = ['type', 'title', 'author', 'postCategory', 'creationDate']
