"""User Views"""
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages

# Models
from Users.models import Profile

# Forms
from Users.forms import ProfileForm

# Exception
from django.db.utils import IntegrityError

from django.http import JsonResponse

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
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error':'Error, usuario o contraseña invalido!'} )

    return render(request,'users/login.html')


def register_view(request):
    """Register view"""
    if request.method =='POST':

        username      = request.POST['username']
        password      = request.POST['passwd']
        password_conf = request.POST['passwd_confirmation']
        
        if password != password_conf:
            return render(request, 'users/register.html', {'error':'Error, las contraseñas que ingresaste no coinciden!'})
        
        try:
            user= User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/register.html', {'error':'Ya existe alguien con ese nombre de usuario :('})

        user.first_name = request.POST['first_name']
        user.last_name  = request.POST['last_name']
        user.email      = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/register.html')


@login_required
def profile_user_view(request):
    """Profile user view"""
    profile = request.user.profile
    user = request.user

    if request.method == 'POST':

        # user.email = request.POST['email']
        # user.username = request.POST['username']

        # user.save()
        # return redirect('profile')
# ---------------------------------------------------------------
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            # profile.picture = data['picture']
            user.username = data['username']
            user.email = data['email']

            user.save()
            profile.save()
            # messages.success(request, 'Tu perfil ha sido actualizado :)')
            # return redirect('home')
    else:
        form = ProfileForm()
# ---------------------------------------------------------------------

    return render(
        request=request,
        template_name='users/profile.html',
        context={
            'profile':profile, 
            'user':request.user,
            'form':form
            }
        )


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


def prueba(request):
    """Test view"""
    return HttpResponse('<h1>Logeado correctamente</h1>')