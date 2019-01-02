from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.conf import settings

User = settings.AUTH_USER_MODEL


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class SignupForm(UserCreationForm):
    pass
