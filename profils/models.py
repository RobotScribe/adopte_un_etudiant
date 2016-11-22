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
    is_student = models.BooleanField
    ecole = models.CharField(null=True, max_length=100)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.user.email
        

