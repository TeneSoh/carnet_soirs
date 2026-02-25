from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
# from django.contrib.auth.models import User
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

    ROLES_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, widget=forms.TextInput())
    role = forms.ChoiceField(
        choices=ROLES_CHOICES, 
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email',  'phone' , 'role','password1', 'password2']
    
    # def save(self , commit=True):
    #     user = super().save(commit=False)
    #     role = self.cleaned_data['role']
    #     if commit:
    #         user.save()
    #         group = Group.objects.get(name=role)
    #         user.groups.add(group)

            # if role == 'admin':
            #     admin_group = Group.objects.get(name='admin')
            #     user.groups.add(admin_group)
            # else:
            #     user_group = Group.objects.get(name='user')
            #     user.groups.add(user_group)