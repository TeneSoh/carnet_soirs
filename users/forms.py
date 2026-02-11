from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control", 
            "placeholder": "votre@email.com",
            "autofocus": True
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control", 
            "placeholder": "Votre mot de passe",
            "autocomplete": "current-password"
        })
    )

    error_messages = {
        "invalid_login": (
            "Veuillez entrer un email et un mot de passe valides. "
            "Notez que les champs peuvent être sensibles à la casse."
        ),
        "inactive": "Ce compte est inactif.",
    }



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']