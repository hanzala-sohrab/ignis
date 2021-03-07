from django import forms
from .models import Event


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location', 'image')
