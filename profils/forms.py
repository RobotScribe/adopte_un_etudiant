from django import forms

class InscriptionEtudiantForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    age = forms.IntegerField()
    photo = forms.ImageField()#l'ajout doit être optionnel
    ecole = forms.CharField()
    description = forms.CharField(label="Description (facultative)")#l'ajout doit être optionnel
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class InscriptionParticulierForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    age = forms.IntegerField()
    photo = forms.ImageField()#l'ajout doit être optionnel
    description = forms.CharField(label="Description (facultative)")#l'ajout doit être optionnel
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
