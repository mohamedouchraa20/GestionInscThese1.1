from django.urls import path
from . import views

urlpatterns = [
    path('Inscription', views.Inscription, name='Inscription'),
    path('Login', views.Login, name='Login'),
    path('', views.Etudiant, name='Etudiant'),
    path('Formulaire',views.Formulaire,name='Formulaire'),
    path('Logout', views.logout, name='Logout')
]