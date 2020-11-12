"""User Views"""
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages

# Models
from Users.models import Profile, Nutriologist

# Exception
from django.db.utils import IntegrityError


# Create your views here.
def landing_view(request):
    """Landing view"""
    return render(request, 'landing.html')


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate (request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('prueba')
        else:
            return render(request, 'users/login.html', {'error':'Error, usuario o contraseña invalido'} )

    return render(request,'users/login.html')


def register_view(request):
    """Register view"""
    return render(request, 'users/register.html')

    
def prueba(request):
    """Test view"""
    return HttpResponse('<h1>Logeado correctamente</h1>')