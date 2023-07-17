from django import template
from trips.models import animals, smoke

register = template.Library()

@register.filter
def animals_tag(x):
    for choice in animals:
        if choice[0] == x:
            return choice[1]
    return ''

@register.filter
def smoke_tag(x):
    for choice in smoke:
        if choice[0] == x:
            return choice[1]
    return ''