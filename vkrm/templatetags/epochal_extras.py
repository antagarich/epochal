from django import template

register = template.Library()


@register.filter(name='subs')
def subs(arg, value):
    return value - arg


@register.filter(name='negate')
def negate(value):
    return -value