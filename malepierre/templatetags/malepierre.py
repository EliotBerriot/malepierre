from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def pretty_integer(value, before='+', after='', empty='&mdash;'):
    if value == 0:
        return mark_safe(empty)
    return '{0}{1}{2}'.format(before, value, after)
