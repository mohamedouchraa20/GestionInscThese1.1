from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


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

            if not nom:
                # return render(request, 'Etudiant/Signup.html', {'nomErr': videErr})
                if not prenom:
                    # return render(request, 'Etudiant/Signup.html', {'prenomErr': videErr})
                    if not email:
                        # return render(request, 'Etudiant/Signup.html', {'emailErr': videErr})
                        if not password:
                            #  return render(request, 'Etudiant/Signup.html', {'passErr': videErr})
                            if not password1:
                                return render(request, 'Etudiant/Signup.html',
                                              {'pass1Err': videErr, 'nomErr': videErr, 'prenomErr': videErr,
                                               'passErr': videErr, 'emailErr': videErr})
                            else:
                                return render(request, 'Etudiant/Signup.html',
                                              {'nomErr': videErr, 'prenomErr': videErr, 'passErr': videErr,
                                               'emailErr': videErr})
                        else:
                            return render(request, 'Etudiant/Signup.html',
                                          {'nomErr': videErr, 'prenomErr': videErr, 'emailErr': videErr})
                    else:
                        return render(request, 'Etudiant/Signup.html', {'nomErr': videErr, 'prenomErr': videErr, })
                else:
                    return render(request, 'Etudiant/Signup.html', {'nomErr': videErr})
            # Rediriger l'utilisateur vers une page de confirmation
            user.save()
            return redirect('Formulaire')
    else:
        form = EtudiantForm()
    return render(request, 'Etudiant/Signup.html', {'form': form})


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


def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'Etudiant/Login.html', {'form': form})

def Formulaire(request):
    return render(request, 'Etudiant/EspacePersonnel/Formulaire.html', {})


