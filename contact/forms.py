from django import forms

from contact.models import Contact


# # Premiere facon
# class ContactForm(forms.Form):
#         nom = forms.CharField(required=True, max_length=30, min_length=2, widget=forms.TextInput(attrs={
#             "class":"nom",
#             "id":"nom",
#             "name":"nom",
#         }))
#         prenom = forms.CharField(required=True, label="Entrer votre Prenom", min_length=2, widget=forms.TextInput(attrs={
#             "class":"prenom",
#             "id":"prenom",
#             "name":"prenom",
#         }))
#         email = forms.EmailField(required=True, label="Entrer votre email", min_length=2, widget=forms.TextInput(attrs={
#             "class":"email",
#             "id":"email",
#             "name":"email",
#         }))
#         pays = forms.CharField(required=True, label="Entrer votre pays", min_length=2, widget=forms.TextInput(attrs={
#             "class":"pays",
#             "id":"pays",
#             "name":"pays",
#         }))
#         phone = forms.CharField(required=True, label="Entrer votre phone", min_length=2, widget=forms.TextInput(attrs={
#             "class":"phone",
#             "id":"phone",
#             "name":"phone",
#         }))
#         ville = forms.CharField(required=True, label="Entrer votre pays", min_length=2, widget=forms.TextInput(attrs={
#             "class":"ville",
#             "id":"ville",
#             "name":"ville",
#         }))
#         rue = forms.CharField(required=True, label="Entrer votre rue", min_length=2, widget=forms.TextInput(attrs={
#             "class":"rue",
#             "id":"rue",
#             "name":"rue",
#             "value":"00-00-00"
#         }))
#         quartier = forms.CharField(required=True, label="Entrer votre quartier", min_length=2, widget=forms.TextInput(attrs={
#             "class":"quartier",
#             "id":"quartier",
#             "name":"quartier",
#         }))


# Deuxieme facon
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["nom", "prenom", "email", "pays", "ville", "phone","quartier", "rue"]
        labels = {
            "nom": "Entrer votre nom",
            "prenom": "Entrer votre prenom", 
            "email": "Entrer votre email", 
            "pays": "Entrer votre pays", 
            "ville": "Entrer votre ville", 
            "phone": "Entrer votre telephone",
            "quartier": "Entrer votre quartier", 
            "rue": "Entrer votre rue",
        }
        widgets = {
            "nom" : forms.TextInput(
                attrs={
                    "class":"nom",
                    "id":"nom"
                }
            ),
            "prenom" : forms.TextInput(
                attrs={
                    "class":"prenom",
                    "id":"prnom"
                }
            ),
            "email" : forms.TextInput(
                attrs={
                    "class":"email",
                    "id":"email"
                }
            ),
            "pays" : forms.TextInput(
                attrs={
                    "class":"pays",
                    "id":"pays"
                }
            ),
            "ville" : forms.TextInput(
                attrs={
                    "class":"ville",
                    "id":"ville"
                }
            ),
            "phone" : forms.TextInput(
                attrs={
                    "class":"phone",
                    "id":"phone"
                }
            ),
            "quartier" : forms.TextInput(
                attrs={
                    "class":"quartier",
                    "id":"quartier"
                }
            ),
            "rue" : forms.TextInput(
                attrs={
                    "class":"rue",
                    "id":"rue"
                }
            )
        }