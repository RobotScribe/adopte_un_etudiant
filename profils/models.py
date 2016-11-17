from django.db import models
from django import forms

class Etudiant(models.Model):
    nom = models.CharField(max_length=42)
    prenom = models.CharField(max_length=42)
    age = models.IntegerField()
    photo = models.ImageField(upload_to="photos/")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'inscription")
    ecole = models.CharField(max_length=100)
    description = models.TextField(null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
