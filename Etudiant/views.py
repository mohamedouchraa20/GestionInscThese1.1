from time import sleep

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.
def Etudiant(request):
    # if login(request,user=authenticate(request,username,password)):
    return render(request, 'Etudiant/Etudiant.html', {})


def Inscription(request):
    if request.method == 'POST':
        if request.method == 'POST':
            nom = request.POST.get('Nom')
            prenom = request.POST.get('Prenom')
            email = request.POST.get('Email')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            user = User.objects.create_user(username=email, email=email, password=password, first_name=prenom,
                                            last_name=nom)
            user = Utilisateur(Nom=nom, Prenom=prenom, email=email, password=password)
            # les erreurs
            videErr = "Ce champs est obligatoires."
            # Vérification de la validité des données
            if password != password1:
                passErr = "Les mots de passe ne correspondent pas."
                return render(request, 'Etudiant/Signup.html', {'passDef': passErr})

            if Utilisateur.objects.filter(email=email):
                emailExist = email + " est déjà utilisé. "
                return render(request, 'Etudiant/Signup.html', {'emailExist': emailExist})

            if not nom or not prenom or not email or not password or not password1:
                return redirect('Inscription')

            # Rediriger l'utilisateur vers une page de confirmation
            else:
                user.save()
                return redirect('Formulaire')

    return render(request, 'Etudiant/Signup.html', {})


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        utilisateur = Utilisateur.objects.get(email=email)
        if Utilisateur.objects.get(email=email) is not None and Utilisateur.objects.all().filter(password=password).exists():
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('Etudiant')
            else:
                return HttpResponse('Email ou mot de passe incorrect.')

    return render(request, 'Etudiant/Login.html', {})


def Logout(request):
    logout(request)
    return redirect('/')


def Formulaire(request):
    return render(request, 'Etudiant/EspacePersonnel/Formulaire.html', {})


"""
        #user = Utilisateur(email=email, password=password)
        user = authenticate(request, username=email, password=password)
        if Utilisateur.objects.all().filter(email=email):
            if Utilisateur.objects.all().filter(password=password).exists():
                login(request, user)
                nomErr = "connecte "
                return redirect('Etudiant')
                #return render(request, 'Etudiant/Login.html', {'nomErr': nomErr})
            else:
                nomErr = "mot de passe inccorect"
                return render(request, 'Etudiant/Etudiant.html', {'nomErr':nomErr})
        else:
            nomErr = "email n'exist pas"
            return render(request, 'Etudiant/Login.html', {'nomErr':nomErr})
"""

"""
def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Etudiant')
            else:
                form.add_error(None, 'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()
    return render(request, 'Etudiant/Login.html', {'form': form})

"""
"""
def Inscription(request):
    form = EtudiantForm()
    return render(request, 'Etudiant/Signup.html', {'form': form})
"""
