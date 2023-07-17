from django import forms
from trips.models import Trip

class AddTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['can_smoke', 'with_animals']