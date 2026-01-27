from django import forms
class ContactForm(forms.Form):
    nom = forms.CharField(required=True, label="Entrer votre nom", max_length=30, min_length=2, widget=forms.TextInput(attrs={
        "class":"nom h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"nom",
        "name":"nom",
    }))
    prenom = forms.CharField(required=True, label="Entrer votre prenom", min_length=2, widget=forms.TextInput(attrs={
        "class":"prenom h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"prenom",
        "name":"prenom",
    }))
    email = forms.EmailField(required=True, label="Entrer votre email", min_length=2, widget=forms.EmailInput(attrs={
        "class":"email h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"email",
        "name":"email",
    }))
    pays = forms.CharField(required=True, label="Entrer votre pays", min_length=2, widget=forms.TextInput(attrs={
        "class":"pays h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"pays",
        "name":"pays",
    }))
    phone = forms.CharField(required=True, label="Entrer votre phone", min_length=2, widget=forms.TextInput(attrs={
        "class":"phone h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"phone",
        "name":"phone",
    }))
    ville = forms.CharField(required=True, label="Entrer votre ville", min_length=2, widget=forms.TextInput(attrs={
        "class":"ville h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"ville",
        "name":"ville",
    }))
    quartier = forms.CharField(required=True, label="Entrer votre quartier", min_length=2, widget=forms.TextInput(attrs={
        "class":"quartier h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"quartier",
        "name":"quartier",
    }))
    rue =  forms.CharField(required=True, label="Entrer votre rue", min_length=2, widget=forms.TextInput(attrs={
        "class":"rue h-10 border-2 bg-gray-50 text-xs border-gray-300 rounded-md w-full",
        "id":"rue",
        "name":"rue",
        "value":"123-56-logpom",
        "placeholder":"rue"
    }))