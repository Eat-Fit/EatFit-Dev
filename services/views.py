"""Services views"""

from django.shortcuts import render

# Create your views here.

def home_view (request):
    """home view"""
    return render(request, 'services/home_page.html')
