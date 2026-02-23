from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context_processors import request
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required , user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
#from django.views import view
from contact.models import Contact
from .forms import ContactForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

"""
user.has_perm('can_delete_contact') --> pour verifier si l'utilisateur a la permission de supprimer un contact
user.has_perm('contact.can_delete_contact') --> pour verifier si l'utilisateur a la permission de supprimer un contact en precisant le nom de l'application
user.has_perm('contact.delete_contact') --> pour verifier si l'utilisateur a la permission de supprimer un contact en precisant le nom de l'application et le nom de la permission

user.all()
    .add(<perm1> , <perm2> , ...)
    .remove(<perm1> , <perm2> , ...)
    .clear()
    .set([<perm1> , <perm2> , ...]) // pour remplacer les permissions de l'utilisateur par une nouvelle liste de permissions


user.groups.set([<group1> , <group2> , ...]) // pour remplacer les groupes de l'utilisateur par une nouvelle liste de groupes
user.groups.add(<group1> , <group2> , ...) // pour ajouter des groupes à l'utilisateur
user.groups.remove(<group1> , <group2> , ...) // pour supprimer des groupes de l'utilisateur
user.groups.clear() // pour supprimer tous les groupes de l'utilisateur

# Récupérer ou créer un groupe
group, created = Group.objects.get_or_create(name="Managers")

permissions = Permission.objects.get(codename__in=["add_contact", "change_contact", "delete_contact"]) // Récupérer les permissions à partir de leurs codenames
permission = Permission.objects.get(codename = "add_contact") // Récupérer la permission à partir de son codename
group.permissions.set(permissions) // Assigner les permissions au groupe

"""

def is_visitor(user) :
    return user.groups.filter(name='visitor').exists()

# Using class Views

# Create your views here.

# @user_passes_test(is_visitor, login_url='login')
@login_required(login_url='login', redirect_field_name='login')
def index(request):
    # Contacts = Contact.objects.all()
    Contacts = Contact.objects.filter(user=request.user).order_by('-id')
    
    
    # ---- Pagination -----
    #items = Contact.objects.all().order_by('id') # Get all items
    paginator = Paginator(Contacts, 5) # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) # Get page object for current page
    
    
    return render(request, "contact/contacts.html", {"contacts": Contacts,  'page_obj': page_obj })


# def create(request) :
#     return render(request , "contact/create_contact.html")


# def store(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)

#         if form.is_valid():

#             # nom = request.POST['nom']
#             # prenom = request.POST['prenom']
#             # email = request.POST['email']
#             # pays = request.POST['pays']
#             # phone = request.POST['phone']
#             # ville = request.POST['ville']
#             # rue = request.POST['rue']
#             # quartier = request.POST['quartier']

#             # nom = form.cleaned_data.get("nom")
#             # prenom = form.cleaned_data.get("prenom")
#             # email = form.cleaned_data.get("email")
#             # pays = form.cleaned_data.get("pays")
#             # phone = form.cleaned_data.get("phone")
#             # ville = form.cleaned_data.get("ville")
#             # rue = form.cleaned_data.get("rue")
#             # quartier = form.cleaned_data.get("quartier")

#             # Contact.objects.create(
#             #     nom=nom,
#             #     prenom=prenom,
#             #     email=email,
#             #     pays=pays,
#             #     phone=phone,
#             #     ville=ville,
#             #     rue=rue,
#             #     quartier=quartier,
#             # )
#             form.save()
#             return redirect("contact")

#     # return redirect('create_contact')
#     return render(request, "contact/create_contact.html", {"form": form})


# class CreateContactView(CreateView):
#     model = Contact
#     form_class = ContactForm
#     template_name = "contact/create_contact.html"
#     success_url = reverse_lazy('contact')

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["form"] = ContactForm()
#         return context
@method_decorator(login_required(login_url='login', redirect_field_name='store-contact'), name='dispatch')
@method_decorator(permission_required(perm='can_add_contact' , raise_exception=True), name='dispatch')
class CreateContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "contact/create_contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user

            contact.save()

            return redirect("contact")
        
        return render(request, "contact/create_contact.html", {"form": form})


# def edit(request, id: int):

#     contact = get_object_or_404(Contact, id=id)

#     if request.method == "POST":
#         # form = ContactForm(request.POST)
#         form = ContactForm(request.POST, instance=contact)
#         if form.is_valid():

#             # nom = request.POST["nom"]
#             # prenom = request.POST["prenom"]
#             # email = request.POST["email"]
#             # pays = request.POST["pays"]
#             # phone = request.POST["phone"]
#             # ville = request.POST["ville"]
#             # rue = request.POST["rue"]
#             # quartier = request.POST["quartier"]

#             # Contact.objects.filter(id=id).update(
#             #     nom=nom,
#             #     prenom=prenom,
#             #     email=email,
#             #     pays=pays,
#             #     phone=phone,
#             #     ville=ville,
#             #     rue=rue,
#             #     quartier=quartier,
#             # )
#             # contact.nom = nom
#             # contact.prenom = prenom
#             # contact.email = email
#             # contact.pays = pays
#             # contact.phone = phone
#             # contact.ville = ville
#             # contact.rue = rue
#             # contact.quartier = quartier

#             # contact.save()
#             form.save()
#             return redirect("contact")

#     # form = ContactForm(initial={
#     #     "nom": contact.nom, 
#     #     "prenom": contact.prenom,
#     #     "email" : contact.email,
#     #     "pays" : contact.pays,
#     #     "phone" : contact.phone,
#     #     "ville" : contact.ville,
#     #     "rue" : contact.email,
#     #     "quartier" : contact.quartier,
#     # })
#     form = ContactForm(instance=contact)
#     return render(
#         request, "contact/edit_contact.html", {"contact": contact, "form": form}
#     )

@method_decorator(login_required(login_url='login' , redirect_field_name='login'), name='dispatch') #on l'utilse lorqu'il s'agit de class view afin de les securiser    
class UpdateContactView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact/edit_contact.html"
    success_url = reverse_lazy('contact')
    context_object_name = "contact"
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ContactForm(instance=contact)
    #     return context


# def delete(request, id: int):
#     try:
#         contact = Contact.objects.filter(id=id)
#         # contact = Contact.objects.get(id=id)

#         if not contact:
#             raise ValueError("Aucune contact trouvé")

#         contact.delete()

#         return redirect("contact")

#     except Contact.DoesNotExist:
#         raise Http404("Pas de contact trouvé")

@method_decorator(permission_required(perm='can_delete_contact' , raise_exception=True), name='dispatch')
class DeleteContactView(DeleteView):
    model = Contact
    # template_name = "contact/contact_confirm_delete.html"
    success_url = reverse_lazy('contact')

# class DeleteContactView(View):
#     def get(self, request, pk:int):
#         try:
#             contact = Contact.objects.filter(id=pk)
#             # contact = Contact.objects.get(id=id)

#             if not contact:
#                 raise ValueError("Aucune contact trouvé")

#             contact.delete()

#             return redirect("contact")

#         except Contact.DoesNotExist:
#             raise Http404("Pas de contact trouvé")


# def show(request, id):

#     contact = get_object_or_404(
#         Contact, id=id
#     )  # avec ceci pas besoin de mettre des try... except

#     return render(request, "contact/show.html", {"contact": contact})

class DetailContactView(DetailView):
    model = Contact
    template_name = "contact/show.html"
    context_object_name = 'contact'
