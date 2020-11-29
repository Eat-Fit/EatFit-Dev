"""User Views"""
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages

# Models
from Users.models import Profile
from services.models import Receta

# Forms
from Users.forms import ProfileForm, NutriologistForm
from services.forms import UpdateRecetaForm

# Exception
from django.db.utils import IntegrityError

from django.http import JsonResponse

from datetime import date

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
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.picture = data['picture']
        
            user.username = data['username']
            user.email = data['email']

            user.save()

            if profile.picture:
                profile.save()
            # messages.success(request, 'Tu perfil ha sido actualizado :)')
            return redirect('home')
    else:
        form = ProfileForm()

    citas = Receta.objects.all().filter(cliente=profile)
    return render(
        request=request,
        template_name='users/profile.html',
        context={
            'profile':profile, 
            'user':request.user,
            'form':form,
            'citas':citas,
            }
        )

@login_required
def profile_nutri_edit_view(request):
    """Profile Nutriologist View"""
    hoy = date.today()
    profile = request.user.profile
    citas_de_hoy = Receta.objects.all().filter(fecha_de_cita__day=hoy.day,estado=True)
    return render(request,'users/profile_nutri_edit_view.html', context={'profile':profile,'citas_hoy':citas_de_hoy})


@login_required
def edit_nutri_profile(request):
    """Profile Nutriologist edit form"""
    profile = request.user.profile
    nutriologist = request.user.profile.nutriologist
    user = request.user

    if request.method == 'POST':
        form = NutriologistForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.picture = data['picture']
            
            user.username = data['username']
            user.email = data['email']
            nutriologist.attention_days = data['attention_days']
            nutriologist.attention_hours = data['attention_hours']
            nutriologist.age = data['age']
            nutriologist.work_approach = data['work_approach']
            nutriologist.cedula_prof_det = data['cedula_prof_det']
            nutriologist.biography = data['biography']

            user.save()
            if profile.picture:
                profile.save()
            nutriologist.save()

            return redirect('profileNutriEdit')
    else:
        form = NutriologistForm()

    return render(  request=request, 
                    template_name='users/profile_nutri_edit_form_view.html', 
                    context={
                        'form':form
                        })

@login_required
def detalle_cita_view(request, id):
    """Ver detalle de cita"""
    current_user = request.user
    receta = Receta.objects.get(id=id)

    if request.method =='POST':
        form = UpdateRecetaForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data

            receta.fecha_de_cita = data['fecha_de_cita']
            receta.hora_de_cita = data['hora_de_cita']
            receta.motivo_de_cita = data['motivo_de_cita']
            receta.dctos_asignados = data['dctos_asignados']
            receta.estado = data['estado']
            receta.activa = data['activa']

            receta.save()
            return redirect('home')
    else:
        form = UpdateRecetaForm()

    return render(request, 'users/detalle_cita.html', {'cita':receta, 'form':form})


@login_required
def citas_detalle_nutri_view(request):
    """Todas las citas del nutriologo"""
    citas_pendientes = Receta.objects.all().filter(nutriologo=request.user.profile.nutriologist, activa=True)
    citas_terminadas = Receta.objects.all().filter(nutriologo=request.user.profile.nutriologist, activa=False)
    return render (
        request, 
        'users/profile_nutri_citas.html',
        context={
            'citas_terminadas':citas_terminadas,
            'citas_pendientes':citas_pendientes,
        })


@login_required
def profile_nutri_view(request, username):
    """Profile Nutriologist View"""
    current_user = request.user
    user = User.objects.get(username=username)
    # post = user.post.all() como ejemplo para conseguir todos los post de user
    if request.method == 'POST':
        date = request.POST['date_selected']
        hour = request.POST['hour_selected']

        cita = Receta.objects.create(nutriologo=user.profile.nutriologist,cliente=current_user.profile, fecha_de_cita=date, hora_de_cita=hour)
        
        return redirect('home')

    return render(request, 'users/profile_nutri_view.html', {'user':user} )



@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')
