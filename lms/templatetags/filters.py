from django import template

register = template.Library()

"""
DIVISION

value ÷ args
"""
@register.filter(name="division")
def division(value, args):
    return round(value / args)

"""
TYPE CHECK

# template file
{% if extra_column|get_type == 'A' %}
   data type A
{% elif extra_column|get_type == 'B' %}
    data type B
{% else %}
    Oh no!
{% endif %}

"""
@register.filter(name="get_type")
def get_type(value):
    return type(value)
