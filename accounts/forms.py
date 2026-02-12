from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["phone", "avatar"]
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Phone Number"}
            ),
        }
