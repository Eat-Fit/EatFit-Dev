"""eatfit URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path


# Static files


# Views
from Users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Users views
    path('', users_views.landing_view, name='landing'),
]
# Comentario de prueba
