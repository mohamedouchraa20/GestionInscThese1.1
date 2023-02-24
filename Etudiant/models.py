from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    def __str__(self):
        return f"{self.id} {self.Nom}"
    objects = models.Manager()