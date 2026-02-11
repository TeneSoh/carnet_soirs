from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm) : 
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : '',
                'placeholder' : 'email',
            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput , max_length=255, required=True)

    class Meta:
        model = User
        fields = ['email']