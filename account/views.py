from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import RegisterForm

# Create your views here.

def register(request) :
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('contact')
            
        return render(request, 'registration/regiter.html', {'form' : form})
    return render(request , 'registration/register.html', {'form' : form})
    # return render(request , 'login.html')