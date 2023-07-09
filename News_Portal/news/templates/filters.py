from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def cenzur(value):
    words_to_cenzur = ['bad', 'words', 'to', 'censor']
    for word in words_to_cenzur:
        value = value.replace(word, '*' * len(word))
    return mark_safe(value)
