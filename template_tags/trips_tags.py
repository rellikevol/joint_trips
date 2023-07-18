from django import template
from trips.models import trip_animals, trip_smoke
from users.models import profile_smoke, profile_animals, profile_music, profile_conversations


register = template.Library()

trips_choice = trip_smoke + trip_animals
users_choice = profile_smoke + profile_animals + profile_music + profile_conversations

@register.filter
def trip_tag(x):
    for choice in trips_choice:
        if choice[0] == x:
            return choice[1]
    return ''

@register.filter
def users_tag(x):
    for choice in users_choice:
        if choice[0] == x:
            return choice[1]
    return ''