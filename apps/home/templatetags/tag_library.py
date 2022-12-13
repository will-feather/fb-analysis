# templatetags/tag_library.py
from django import template

register = template.Library()

@register.filter
def to_float(string):
    return float(string.replace('%', ''))
