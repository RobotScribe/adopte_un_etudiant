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
    
    
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Pseudo")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    

class AnnonceForm(forms.Form) :
    titre = forms.CharField(max_length=200)
    #boulot = forms.ModelChoiceField(queryset=('Ménage','Déménagement','Plomberie','Jardinage','Cours','Service d\'aide à la personne','autre...'), empty_label=None)
    annonce = forms.CharField(widget=forms.Textarea, label="Décrivez votre petite annonce")
    prix = forms.DecimalField(max_digits=5,decimal_places=2)
    lieux = forms.CharField(max_length=50)
    distance_max = forms.IntegerField(label="Indiquez la distance maximale en km que vous pouvez faire pour chercher un étudiant. Mettez 0 si vous ne voulez pas aller le chercher")
    
    
class PostulerAnnonceForm(forms.Form):
    Commentaires = forms.CharField(label = 'expliquez pourquoi le personne qui a postée cette annonce devrait vous prendre (facultatif)', required = False )
    
class ModifierProfilForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label = "Mot de passe actuel")
    pseudo = forms.CharField(label = "Nouveau pseudo")
    new_password = forms.CharField(widget=forms.PasswordInput, label="Rentrez votre nouveau mot de passe")
    photo = forms.ImageField(required=False, label = "Nouvelle photo (facultative)")
    description = forms.CharField(required=False,label="Nouvelle description (facultative)")
    is_student = forms.BooleanField(required=False,label = "cochez si vous êtes étudiant")
    école = forms.CharField(required=False,label = "rentrez votre école si vous êtes étudiant")
    

class ModifierAnnonceForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label = "Mot de passe actuel")
    titre = forms.CharField(max_length=200)
    annonce = forms.CharField(widget=forms.Textarea, label="Décrivez votre petite annonce")
    prix = forms.DecimalField(max_digits=5,decimal_places=2)
    lieux = forms.CharField(max_length=50)
    distance_max = forms.IntegerField(label="Indiquez la distance maximale en km que vous pouvez faire pour chercher un étudiant. Mettez 0 si vous ne voulez pas aller le chercher")
    
class SupprimerAnnonceForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label = "Mot de passe actuel")
    












    
    
