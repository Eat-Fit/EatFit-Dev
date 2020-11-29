"""eatfit URL Configuration"""

# Django
from django.contrib import admin
from django.urls import path


# # Static files
from django.conf import settings
from django.conf.urls.static import static

# Views
from Users import views as users_views
from services import views as services_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # USER VIEWS---------------------------------------------------
    path('',           users_views.landing_view , name='landing'),
    path('login/',     users_views.login_view , name='login'),
    path('logout/',    users_views.logout_view, name='logout'),
    path('register/',  users_views.register_view , name='register'),
    path('mi-perfil/', users_views.profile_user_view, name='profile'),
    path('mi-perfil/nutri/', users_views.profile_nutri_edit_view, name='profileNutriEdit'),
    path('mi-perfil/nutri/editar/', users_views.edit_nutri_profile, name='updateProfileNutri'),
    path('mi-perfil/nutri/citas/', users_views.citas_detalle_nutri_view, name='citasNutri'),
    path('mi-perfil/detalle-cita/<str:id>', users_views.detalle_cita_view, name='detalleCita'),
    path('perfil-nutri/<str:username>/', users_views.profile_nutri_view, name='profileNutri'),
    # END USER VIEWS-----------------------------------------------



    # Services views
    path('home/', services_views.home_view, name='home'),
    
    
    # RESTORE PASSWORD VIEWS--------------------------------------------------------
    path('password_change/',
    auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
    name='password_change' ),
    # Uriel

    path('password_change/done/',
    auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
    name='password_change_done' ),
    # Uriel


    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
    name='password_reset' ),
    # Netzy

    path('password_reset/done',
    auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done' ),
    # Niezty


    path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),
    # Nietzy

    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),
    # END RESTORE PASSWORD----------------------------------------------------------
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)