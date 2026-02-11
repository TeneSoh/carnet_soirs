from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from users.forms import LoginForm, RegisterForm

# Create your views here.

def signIn(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect('contact')
   
        return render(request=request, template_name='users/login.html', context={'form': form})
    
    return render(request=request, template_name='users/login.html', context={'form': form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
   
        return render(request=request, template_name='users/register.html', context={'form': form})
    
    return render(request=request, template_name='registration/register.html', context={'form': form}  )

def disconnect(request):
    logout(request)
    return redirect('login')