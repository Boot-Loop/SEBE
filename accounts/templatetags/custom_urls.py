
from django.urls import reverse
from django import template
register = template.Library()

@register.simple_tag
def url_getargs(view_name, args):
    return reverse(view_name) + args