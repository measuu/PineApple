from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-input", "placeholder": "Email"}),
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Phone Number"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Username"}
            ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Password"}
        )
    )
