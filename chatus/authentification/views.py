from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from authentification.forms import LoginForm, SignupForm

def login_page(request):
    form = LoginForm()
    message = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('public_chat')

        
        else:
            message = 'Identifiants invalides'

    return render(request, 'authentification/login_page.html', 
                  context={'form': form, 'message': message})

def home(request):
    return render (request, 'authentification/home.html')

def signup_page(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('public_chat')
        
    return render(request, 'authentification/signup_page.html',
                  context={'form': form})

def logout_user(request):
        logout(request)
        return redirect('home')