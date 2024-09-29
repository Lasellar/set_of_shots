from django import forms

from .models import Event, Post


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'title', 'description',
            'slug', 'start', 'place', 'is_published', 'image'
        )
        widgets = {
            'title': forms.Textarea(
                attrs={'rows': 3, 'cols': 80}),
            'description': forms.Textarea(
                attrs={'rows': 18, 'cols': 80}),
            'slug': forms.Textarea(
                attrs={'rows': 2, 'cols': 80}),
        }
