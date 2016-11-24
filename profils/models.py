from django.db import models
from django import forms
from django.contrib.auth.models import User

"""
Les attributs de la classe User sont :
    -username
    -first_name
    -last_name
    -email
    -password
    -is_staff
    -is_active
    -is_superuser
    -last_login
    -date_joined
    -user_permissions
    -groups
"""

class Profil(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    photo = models.ImageField(upload_to="photos/", null=True)
    is_student = models.BooleanField()
    ecole = models.CharField(null=True, max_length=100)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username
        

        
class Annonce (models.Model) :
	""" Classe qui va gérer tout ce qui concerne les articles"""
	titre = models.CharField(max_length=200)
	 #boulot = models.CharField(max_length=50)
	annonce = models.TextField(null=False)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name = "Date de dépôt")
	prix = models.DecimalField(max_digits=5,decimal_places=2)
	annonceur = models.CharField(max_length=100)
    etudiant = models.CharField(max_length=100, null=True)
	lieux = models.CharField(max_length=50)
	distance_max = models.IntegerField()
	numero = models.IntegerField()
    #etat ne peux prendre que 3 valeurs : "a faire", "fait", "en cours"
    etat = models.CharField(max_length=10)


	def __str__(self) :
		return self.titre 

