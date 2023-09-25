
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser
from captcha.fields import CaptchaField

class CaptchaForm(forms.Form):
    captcha = CaptchaField()


class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ['username', 'email', 'password1', 'password2', 'mobile', 'image']

