from django.shortcuts import redirect, render
from django.contrib import messages
from contact.models import Contact
# Create your views here.
def index(request):
    return render(request, "contact/contacts.html")


# def create(request) : 
#     return render(request , "contact/create_contact.html")

def store(request) : 
    if(request.method == 'POST') : 

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        pays = request.POST['pays']
        phone = request.POST['phone']
        ville = request.POST['ville']
        rue = request.POST['rue']

        Contact.objects.create(
            nom = nom,
            prenom = prenom,
            email = email,
            pays = pays,
            phone = phone,
            ville = ville,
            rue = rue,
        )

        return redirect('contact')


    return render(request , "contact/create_contact.html")


def edit(request) : 
    pass

def delete(request) : 
    pass

# def add(a,b):
#     return a + b

# a = 3
# b = 8
# add(a=a, b=b)

def delate(request):
    pass