from django.shortcuts import render

# Create your views here.


def landing_view(request):
    """Landing view"""
    return render(request, 'landing.html')


def login_view(request):
    """Login view"""
    return render(request,'users/login.html')


def register_view(request):
    """Register view"""
    return render(request, 'users/register.html')

    
def hello_world(request):
    """Test view"""
    return HttpResponse('<h1>Hola mundo jeje</h1>')