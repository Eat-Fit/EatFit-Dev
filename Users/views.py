from django.shortcuts import render

# Create your views here.


def landing_view(request):
    """Landing view"""
    return render(request, 'landing.html')
    
def hello_world(request):
    return HttpResponse('<h1>Hola mundo jeje</h1>')