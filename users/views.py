from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import request

# from django.contrib.auth import login, logout, authenticate
from users.forms import LoginForm, RegisterForm
# from users.forms import LoginForm, RegisterForm

# Create your views here.


def signIn(request) : 

    form = LoginForm()

    if request.method == "POST" :
        form = LoginForm(request.POST)
        if form.is_valid() : 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request , username = email , password = password)
            if user is not None : 
                login(request , user)
                return redirect("contact")
        return render(request , 'users/login.html' , {"form" : form})

    return render(request , 'users/login.html' , {"form" : form})



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

def disconnect(request) :
    logout(request)
    return redirect('login')