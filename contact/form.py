from django.forms import ValidationError
# from contact.form import ContactForm
from contact.models import Contact
# from django.forms import CharField
from django import forms


# class ContactForm(forms.Form):
#     nom = forms.CharField(required=True,label='Entrez votre nom' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'nom h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full ',
#             'id': 'nom',
#             'placeholder': 'Nom',
#         }
#     ))
#     prenom = forms.CharField(required=True,label='Entrez votre prenom' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'prenom h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'prenom',
#             'placeholder': 'prenom',
#         }
#     ))
#     email = forms.EmailField(required=True,label='Entrez votre email' , max_length=30 , min_length=2 , widget=forms.EmailInput(
#         attrs={
#             'class': 'email h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'email',
#             'placeholder': 'email',
#         }
#     ))
#     pays = forms.CharField(required=True,label='Entrez votre pays' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'pays h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'pays',
#             'placeholder': 'pays',
#         }
#     ))
#     phone = forms.CharField(required=True,label='Entrez votre phone' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'phone h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'phone',
#             'placeholder': 'phone',
#             'type' : 'number',
#         }
#     ))
#     ville = forms.CharField(required=True,label='Entrez votre ville' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'phone h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'ville',
#             'placeholder': 'ville',
#             'type' : 'text',
#         }
#     ))
#     quartier = forms.CharField(required=True,label='Entrez votre quartier' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'quartier h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'quartier',
#             'placeholder': 'quartier',
#         }
#     ))
#     rue = forms.CharField(required=True,label='Entrez votre rue' , max_length=30 , min_length=2 , widget=forms.TextInput(
#         attrs={
#             'class': 'rue h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
#             'id': 'rue',
#             'placeholder': 'rue',
#         }
    # ))

class ContactForm(forms.ModelForm) : 
    class Meta:
        model = Contact
        fields = ['nom' , 'prenom' , 'email' , 'pays' , 'phone' , 'ville' , 'quartier' , 'rue']
        labels = {
            'nom' : 'Entrez votre nom',
            'prenom' : 'Entrez votre prenom',
            'email' : 'Entrez votre email',
            'pays' : 'Entrez votre pays',
            'phone' : 'Entrez votre phone',
            'ville' : 'Entrez votre ville',
            'quartier' : 'Entrez votre quartier',
            'rue' : 'Entrez votre rue',
        }
        widgets = {
            'nom' : forms.TextInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "nom"
            }),
            'prenom' : forms.TextInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "prenom"
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "email"
            }),
            'pays' : forms.TextInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "pays"
            }),
            'phone' : forms.NumberInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "phone"
            }),
            'ville' : forms.TextInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "ville"
            }),
            'quartier' : forms.TextInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "quartier"
            }),
            'rue' : forms.TextInput(attrs={
                'class' : 'h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full',
                'placeholder' : "rue"
            }),
        }


    def clean_nom(self) : 
        nom = self.cleaned_data["nom"]
        if nom and len(nom) < 2 : 
            raise ValidationError(message="Le nom est trop court")
        return nom
    

    def clean_prenom(self) : 
        prenom = self.cleaned_data["prenom"]
        if prenom and len(prenom) < 2 : 
            raise ValidationError(message="Le prenom est trop court")
        return prenom
    
    def clean_email(self) : 
        email = self.cleaned_data["email"]
        if email and len(email) < 2 : 
            raise ValidationError(message="Le email est trop court")
        return email
    
    def clean_pays(self) : 
        pays = self.cleaned_data["pays"]
        if pays and len(pays) < 2 : 
            raise ValidationError(message="Le pays est trop court")
        return pays
    
    def clean_phone(self) : 
        phone = self.cleaned_data["phone"]
        if phone and len(phone) < 2 : 
            raise ValidationError(message="Le phone est trop court")
        return phone
    
    def clean_ville(self) : 
        ville = self.cleaned_data["ville"]
        if ville and len(ville) < 2 : 
            raise ValidationError(message="Le ville est trop court")
        return ville
    
    def clean_quartier(self) : 
        quartier = self.cleaned_data["quartier"]
        if quartier and len(quartier) < 2 : 
            raise ValidationError(message="Le quartier est trop court")
        return quartier
    
    def clean_rue(self) : 
        rue = self.cleaned_data["rue"]
        if rue and len(rue) < 2 : 
            raise ValidationError(message="Le rue est trop court")
        return rue
    

