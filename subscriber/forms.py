from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from flatpickr import DatePickerInput

from django.contrib.auth.models import User

# first time register form
class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


