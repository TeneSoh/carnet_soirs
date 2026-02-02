from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.template.context_processors import request
from django.http import Http404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from contact.models import Contact
from contact.form import ContactForm
# from contact.views import DeleteContactView
# from contact.views import UpdateContactView
# from contact.views import CreateContactView, ListContact


# Create your views here.
# def index(request):
#     contacts = Contact.objects.all()
#     return render(request, "contact/contacts.html" , {'contacts' : contacts})

#Utilisation des class views 

# class ListContact(ListView) : 
#     model = Contact
#     template_name = "contact/contacts.html"
#     context_object_name = "contacts"

# deuxieme methode

class ListContact(View) : 
    def get(self , request) : 
         contacts = Contact.objects.all()
         return render(request , "contact/contacts.html" , {"contacts" : contacts})

# def create(request) : 
#     return render(request , "contact/create_contact.html")

# def store(request) : 
#     form = ContactForm()
#     if (request.method == 'POST') : 
#         form = ContactForm(request.POST)
#         if form.is_valid() : 
#             # nom = request.POST.get('nom')
#             # prenom = request.POST['prenom']
#             # email = request.POST['email']
#             # pays = request.POST['pays']
#             # phone = request.POST['phone']
#             # ville = request.POST['ville']
#             # rue = request.POST['rue']
#             # quartier = request.POST['quartier']


#             #deuxieme methode avec forms.Form

#             # nom = form.cleaned_data.get('nom')
#             # prenom = form.cleaned_data.get('prenom')
#             # email = form.cleaned_data.get('email')
#             # pays = form.cleaned_data.get('pays')
#             # phone = form.cleaned_data.get('phone')
#             # ville = form.cleaned_data.get('ville')
#             # rue = form.cleaned_data.get('rue')
#             # quartier = form.cleaned_data.get('quartier')

#             # Contact.objects.create(
#             #     nom = nom,
#             #     prenom = prenom,
#             #     email = email,
#             #     pays = pays,
#             #     phone = phone,
#             #     ville = ville,
#             #     rue = rue,
#             #     quartier = quartier,
#             # )


#             #troisieme methode avec forms.Form
#             form.save()

#             return redirect('contact')


#     # return redirect('create_contact')
#     return render(request=request, template_name='contact/create_contact.html' , context={"form" : form})

# class CreateContactView(CreateView) : 
#     model = Contact
#     form_class = ContactForm
#     template_name = "contact/create_contact.html"
#     success_url = reverse_lazy("contact")

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["forms"] = ContactForm()
#         return context
    
# deuxieme methode 

class CreateContactView(View) : 
     def get(self , request) : 
        form = ContactForm(request.POST)
        return render(request, 'contact/create_contact.html' , {"form" : form})


     def post(self , request) : 
        form = ContactForm(request.POST)
        if form.is_valid() : 
            form.save()

            return redirect('contact')
        return render(request, 'contact/create_contact.html' , {"form" : form})






def edit(request , id:int) : 
    form = ContactForm()
    contact = get_object_or_404(Contact , id = id)

    if (request.method == 'POST') : 
        form = ContactForm(request.POST , instance=contact)
        if form.is_valid() : 

            # methode 1 recuperation des donnees
            # nom = request.POST['nom']
            # prenom = request.POST['prenom']
            # email = request.POST['email']
            # pays = request.POST['pays']
            # phone = request.POST['phone']
            # ville = request.POST['ville']
            # rue = request.POST['rue']
            # quartier = request.POST['quartier']

            # methode 2 recuperation des donnees
            # nom = form.cleaned_data.get('nom')
            # prenom = form.cleaned_data.get('prenom')
            # email = form.cleaned_data.get('email')
            # pays = form.cleaned_data.get('pays')
            # phone = form.cleaned_data.get('phone')
            # ville = form.cleaned_data.get('ville')
            # rue = form.cleaned_data.get('rue')
            # quartier = form.cleaned_data.get('quartier')


            # methode 1 pour mettre a jour
            # Contact.objects.filter(id=id).update(
            #     nom = nom,
            #     prenom = prenom,
            #     email = email,
            #     pays = pays,
            #     phone = phone,
            #     ville = ville,
            #     rue = rue,
            #     quartier = quartier,
            # )

            # methode 2 pour mettre a jour
            # contact.nom = nom
            # contact.prenom = prenom
            # contact.email = email
            # contact.pays = pays
            # contact.phone = phone
            # contact.ville = ville
            # contact.rue = rue
            # contact.quartier = quartier
            # contact.save()

            form.save()
            return redirect('contact')


    # lier a la methode 2 de recuperation des donnees
    # form = ContactForm(
    #     initial={
    #         "nom" : contact.nom,
    #         "prenom" : contact.prenom,
    #         "email" : contact.email,
    #         "pays" : contact.pays,
    #         "phone" : contact.phone,
    #         "ville" : contact.ville,
    #         "rue" : contact.rue,
    #         "quartier" : contact.quartier,
    #     }
    # )

    form = ContactForm(instance=contact)
    return render (request , "contact/edit_contact.html" , {'form' : form})
    # return render (request , "contact/edit_contact.html" , {'contact' : contact})


# en heritant de UpdateView
class UpdateContactView(UpdateView) : 
    model = Contact
    form_class = ContactForm
    template_name = "contact/edit_contact.html"
    success_url = reverse_lazy("contact")


# en heritant de view

# class UpdateContactView(View) : 
#      def get(self , request , id:int) : 
#         contact = get_object_or_404(Contact , id = id)
#         form = ContactForm(instance=contact)
#         return render(request, 'contact/edit_contact.html' , {"form" : form})


#      def post(self , request,id:int) : 
#         contact = get_object_or_404(Contact , id = id)
#         form = ContactForm(request.POST , instance=contact)
#         if form.is_valid() : 
#             form.save()

#             return redirect('contact')




# def delete(request , id:int) : 
#     try : 
#         contact = Contact.objects.filter(id = id)
#         # contact = Contact.objects.get(id=id)
        
#         if not contact : 
#             raise ValueError("Aucune contact trouvé")

#         contact.delete()

#         return redirect("contact")

#     except Contact.DoesNotExist : 
#         raise Http404("Pas de contact trouvé")



class DeleteContactView(DeleteView):
    model = Contact
    template_name = "contact/contact_confirm_delete.html"
    success_url = reverse_lazy("contact")



# def show(request , id) : 

#         contact = get_object_or_404(Contact , id = id) #avec ceci pas besoin de mettre des try... except

#         return render(request , 'contact/show.html' , {'contact' : contact})

class ShowViewContact(DetailView):
    model = Contact
    template_name = 'contact/show.html'
    context_object_name = "contact"
