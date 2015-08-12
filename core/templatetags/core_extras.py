from django import template

register = template.Library()

@register.filter(name='count')
def count(value, arg):
    """Removes all values of arg from the given string"""
    # for each in value:
        # print each
    return value