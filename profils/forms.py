from django import forms

class InscriptionForm(forms.Form):
    pseudo = forms.CharField()
    prenom = forms.CharField()
    nom = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    photo = forms.ImageField(required=False)
    description = forms.CharField(required=False,label="Description (facultative)")
    is_student = forms.BooleanField(required=False,label = "cochez si vous êtes étudiant")
    école = forms.CharField(required=False,label = "rentrez votre école si vous êtes étudiant")
    

