from django.shortcuts import render  
from .models import Contact

# Create your views here.
def index(request):
    return render(request=request, template_name='contact/contacts.html')

def show(request, id):
    contact = Contact.objects.get(id=id)
    context = {"contact": contact}
    return render(request=request, template_name="contact/shows.html",context=context)

