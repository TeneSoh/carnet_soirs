from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "contact/contacts.html")

# def add(a,b):
#     return a + b

# a = 3
# b = 8
# add(a=a, b=b)

def delate(request):
    pass