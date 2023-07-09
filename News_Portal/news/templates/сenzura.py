from django import template
from django.utils.safestring import mark_safe

from News_Portal.news.templates.Bran import matuk

register = template.Library()


@register.filter
def censor(value):
    words_to_censor = matuk
    for word in words_to_censor:
        value = value.replace(word, '*' * len(word))
    return mark_safe(value)
