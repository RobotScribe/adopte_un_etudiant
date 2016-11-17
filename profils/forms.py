from django import forms

class InscriptionEtudiantForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    age = forms.IntegerField()
    photo = forms.ImageField()
    ecole = forms.CharField()
    description = forms.CharField(label="Description (facultative)")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
