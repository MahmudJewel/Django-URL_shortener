from django import forms

from .models import ShortURLS


class ShortenerForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = ShortURLS

        fields = ('long_url',)
