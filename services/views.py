"""Services views"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# MODELS
from Users.models import Nutriologist

# Create your views here.

@login_required
def home_view (request):
    """home view"""
    nutri = Nutriologist.objects.all().filter(active=True).order_by('?')
    return render(request, 'services/home_page.html', {'nutris': nutri})
