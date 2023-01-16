from django import template

register = template.Library()


@register.filter
def round_floor(value):
    """Returns rounded down number """
    return int(value)


@register.filter
def get_fractional(value):
    """Returns fractional part of a number """
    if value - int(value):
        return int((value - int(value))*10)
    return ""


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def add(value, arg):
    return value + arg
