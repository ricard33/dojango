from django.template import Library

from dojango.util import json_encode, version_cmp

register = Library()

@register.filter
def json(input):
    return json_encode(input)

@register.filter
def version_upper_than(value, arg):
    """Test if a version string is upper than the one given as argument."""
    return version_cmp(value, arg) > 0
