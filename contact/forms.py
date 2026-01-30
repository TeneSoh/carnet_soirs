from django.forms import ValidationError
from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     nom = forms.CharField(required=True, label="Entrer votre nom", max_length=30, min_length=2, widget=forms.TextInput(attrs={
#         "class":"nom h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"nom",
#         "name":"nom",
#     }))
#     prenom = forms.CharField(required=True, label="Entrer votre prenom", min_length=2, widget=forms.TextInput(attrs={
#         "class":"prenom h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"prenom",
#         "name":"prenom",
#     }))
#     email = forms.EmailField(required=True, label="Entrer votre email", min_length=2, widget=forms.EmailInput(attrs={
#         "class":"email h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"email",
#         "name":"email",
#     }))
#     pays = forms.CharField(required=True, label="Entrer votre pays", min_length=2, widget=forms.TextInput(attrs={
#         "class":"pays h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"pays",
#         "name":"pays",
#     }))
#     phone = forms.CharField(required=True, label="Entrer votre phone", min_length=2, widget=forms.TextInput(attrs={
#         "class":"phone h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"phone",
#         "name":"phone",
#     }))
#     ville = forms.CharField(required=True, label="Entrer votre ville", min_length=2, widget=forms.TextInput(attrs={
#         "class":"ville h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"ville",
#         "name":"ville",
#     }))
#     quartier = forms.CharField(required=True, label="Entrer votre quartier", min_length=2, widget=forms.TextInput(attrs={
#         "class":"quartier h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"quartier",
#         "name":"quartier",
#     }))
#     rue =  forms.CharField(required=True, label="Entrer votre rue", min_length=2, widget=forms.TextInput(attrs={
#         "class":"rue h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
#         "id":"rue",
#         "name":"rue",
#         "value":"123-56-logpom",
#         "placeholder":"rue"
#     }))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["nom", "prenom", "email", "pays", "phone", "ville", "quartier", "rue"]
        labels = {
            "nom": "Entrer votre nom",
            "prenom": "Entrer votre prenom",
            "email": "Entrer votre email",
            "pays" : "Entrer votre pays",
            "phone" : "Entrer votre Numero de telephone",
            "ville": "Entrer votre ville",
            "quartier": "Entrer votre quartier",
            "rue" : "Entre votre rue",
        }
        widgets = {
            "nom":forms.TextInput(
                attrs={
                    "class":"nom",
                    "id":"nom"
                }
            ),
            "prenom":forms.TextInput(
                attrs={
                    "class":"prenom",
                    "id":"prenom"
                }
            ),
            "email":forms.EmailInput(
                attrs={
                    "class":"email",
                    "id":"email"
                }
            ),
            "pays":forms.TextInput(
                attrs={
                    "class":"pays",
                    "id":"pays"
                }
            ),
            "phone":forms.TextInput(
                attrs={
                    "class":"phone",
                    "id":"phone"
                }
            ),
            "ville":forms.TextInput(
                attrs={
                    "class":"ville",
                    "id":"ville"
                }
            ),
            "quartier":forms.TextInput(
                attrs={
                    "class":"quartier",
                    "id":"quartier"
                }
            ),
            "rue":forms.TextInput(
                attrs={
                    "class":"rue",
                    "id":"rue"
                }
            ),
        }

    def clean_nom(self):
        nom = self.cleaned_data["nom"]
        if nom and len(nom) < 2:
            raise ValidationError(message="le nom doit etre supperieur a 2")
        return nom