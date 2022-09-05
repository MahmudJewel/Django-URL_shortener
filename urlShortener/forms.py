from django import forms

from .models import ShortURLS


class ShortenerForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    short_url = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'size': '15', "class": "form-control form-control-lg", "placeholder": "Enter Custom URL (Optional)"}))
    expiration_day = forms.IntegerField(required=False, initial=1, widget=forms.NumberInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Enter expiration day (Optional)"}))

    class Meta:
        model = ShortURLS

        fields = ('long_url','short_url','expiration_day')
