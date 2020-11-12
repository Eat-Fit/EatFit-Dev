"""Services views"""

from django.shortcuts import render

# MODELS
from Users.models import Nutriologist

# Create your views here.

def home_view (request):
    """home view"""
    nutri = Nutriologist.objects.all().filter(active=True).order_by('?')
    return render(request, 'services/home_page.html', {'nutris': nutri})
