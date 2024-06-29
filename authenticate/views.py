from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import loginform

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or desired URL after successful login
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid email or password. Please check the input.')
    else:
        form = loginform()
    
    return render(request, 'authenticate/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')