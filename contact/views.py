from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context_processors import request
from django.http import Http404
from contact.models import Contact
# Create your views here.
def index(request):
    Contacts = Contact.objects.all().order_by('-id')
    
    
    # ---- Pagination -----
    #items = Contact.objects.all().order_by('id') # Get all items
    paginator = Paginator(Contacts, 2) # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) # Get page object for current page
    
    
    return render(request, "contact/contacts.html", {"contacts": Contacts,  'page_obj': page_obj })


# def create(request) : 
#     return render(request , "contact/create_contact.html")

def store(request) : 
    if (request.method == 'POST') : 

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        pays = request.POST['pays']
        phone = request.POST['phone']
        ville = request.POST['ville']
        rue = request.POST['rue']
        quartier = request.POST['quartier']

        Contact.objects.create(
            nom = nom,
            prenom = prenom,
            email = email,
            pays = pays,
            phone = phone,
            ville = ville,
            rue = rue,
            quartier = quartier,
        )

        return redirect('contact')


    # return redirect('create_contact')
    return render(request=request, template_name='contact/create_contact.html')


def edit(request, id:int) : 
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        pays = request.POST['pays']
        phone = request.POST['phone']
        ville = request.POST['ville']
        rue = request.POST['rue']
        quartier = request.POST['quartier']


        contact.nom = nom
        contact.prenom = prenom
        contact.email = email
        contact.pays = pays
        contact.phone = phone
        contact.ville = ville
        contact.rue = rue
        contact.quartier = quartier

        contact.save()
        
        return redirect('contact')
    return render(request, 'contact/edit.html', {'contact':contact})
        

def show(request, id:int) : 
    contact = get_object_or_404(Contact, id=id)
    
    return render (request=request, template_name='contact/show.html', context={'contact':contact})


def delete(request, id:int) : 
    try:
        contact = Contact.objects.filter(id=id)
        if not contact :
            raise ValueError('Aucun contact trouve')
        contact.delete()
        return redirect('contact')
    except ValueError as ve:
        print(f"{ve}")
    except Exception as e :
        print(f"{e}")



# def add(a,b):
#     return a + b

# a = 3
# b = 8
# add(a=a, b=b)