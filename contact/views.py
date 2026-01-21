from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.template.context_processors import request
from django.http import Http404
from contact.models import Contact
from .forms import ContactForm


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, "contact/contacts.html", {"contacts": contacts})


# def create(request) :
#     return render(request , "contact/create_contact.html")


def store(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            # nom = request.POST['nom']
            # prenom = request.POST['prenom']
            # email = request.POST['email']
            # pays = request.POST['pays']
            # phone = request.POST['phone']
            # ville = request.POST['ville']
            # rue = request.POST['rue']
            # quartier = request.POST['quartier']

            nom = form.cleaned_data.get("nom")
            prenom = form.cleaned_data.get("prenom")
            email = form.cleaned_data.get("email")
            pays = form.cleaned_data.get("pays")
            phone = form.cleaned_data.get("phone")
            ville = form.cleaned_data.get("ville")
            rue = form.cleaned_data.get("rue")
            quartier = form.cleaned_data.get("quartier")

            Contact.objects.create(
                nom=nom,
                prenom=prenom,
                email=email,
                pays=pays,
                phone=phone,
                ville=ville,
                rue=rue,
                quartier=quartier,
            )

            return redirect("contact")

    # return redirect('create_contact')
    return render(request, "contact/create_contact.html", {"form": form})


def edit(request, id: int):

    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            nom = request.POST["nom"]
            prenom = request.POST["prenom"]
            email = request.POST["email"]
            pays = request.POST["pays"]
            phone = request.POST["phone"]
            ville = request.POST["ville"]
            rue = request.POST["rue"]
            quartier = request.POST["quartier"]

            Contact.objects.filter(id=id).update(
                nom=nom,
                prenom=prenom,
                email=email,
                pays=pays,
                phone=phone,
                ville=ville,
                rue=rue,
                quartier=quartier,
            )
            # contact.nom = nom
            # contact.prenom = prenom
            # contact.email = email
            # contact.pays = pays
            # contact.phone = phone
            # contact.ville = ville
            # contact.rue = rue
            # contact.quartier = quartier

            # contact.save()

            return redirect("contact")

    form = ContactForm(initial={
        "nom": contact.nom, 
        "prenom": contact.prenom,
        "email" : contact.email,
        "pays" : contact.pays,
        "phone" : contact.phone,
        "ville" : contact.ville,
        "rue" : contact.email,
        "quartier" : contact.quartier,
    })

    return render(
        request, "contact/edit_contact.html", {"contact": contact, "form": form}
    )


def delete(request, id: int):
    try:
        contact = Contact.objects.filter(id=id)
        # contact = Contact.objects.get(id=id)

        if not contact:
            raise ValueError("Aucune contact trouvé")

        contact.delete()

        return redirect("contact")

    except Contact.DoesNotExist:
        raise Http404("Pas de contact trouvé")


def show(request, id):

    contact = get_object_or_404(
        Contact, id=id
    )  # avec ceci pas besoin de mettre des try... except

    return render(request, "contact/show.html", {"contact": contact})
