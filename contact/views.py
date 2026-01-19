from django.shortcuts import render
from .models import Contact

# Create your views here.
def formulaire_contact(request):
    # if request.method == "POST":
    #     # Récupérer les données du formulaire
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     phone = request.POST.get("phone")
    #     country = request.POST.get("country")
    #     city = request.POST.get("city")
    #     quartier = request.POST.get("quartier")

    #     # Ici, vous pouvez enregistrer les données dans la base de données
    #     # Par exemple, en utilisant un modèle Contact (à créer dans models.py)

    #     # from .models import Contact
    #     # contact = Contact(
    #     #     name=name,
    #     #     email=email,
    #     #     phone=phone,
    #     #     country=country,
    #     #     city=city,
    #     #     quartier=quartier
    #     # )
    #     # contact.save()
    #     messages.success(request, "Contact enregistré avec succès.")
    return render(request, 'contact/formulaire.html')

def infos_contact(request):
    return render(request, 'contact/contacts.html')