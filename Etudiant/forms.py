from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import  *
class EtudiantForm(UserCreationForm):
    Nom = forms.CharField(max_length=30, required=True, help_text='')
    Prenom = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=254, required=True, help_text='')

    class Meta:
        model = User
        fields = ('Nom', 'Prenom', 'email', 'password')


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        label='Nom d\'utilisateur',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Mot de passe',
        strip=False,
        widget=forms.PasswordInput,
    )


"""
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('Nom', 'Prenom', 'email', 'phone', 'Mot_de_pass')
"""


"""
class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
"""

