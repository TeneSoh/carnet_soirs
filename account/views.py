from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import RegisterForm

# Create your views here.

def register(request) :
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            # user = form.save()
            form.save()
            # login(request, user)

            return redirect('login')


        return render(request , 'registration/register.html', {'form': form})
    return render(request , 'registration/register.html', {'form': form})


def disconnect(request):
    logout(request)
    return redirect('login')
