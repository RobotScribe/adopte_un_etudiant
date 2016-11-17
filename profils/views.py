from django.shortcuts import render
from django.http import HttpResponse
from profils.forms import InscriptionEtudiantForm
from profils.models import Etudiant

def home(request):
    return render(request, 'base.html', locals())
 
def inscription(request):
    return render(request, 'profils/inscription.html', locals()) 
    
def inscription_etudiant(request):
    sauvegarde = False
    
    if request.method == "POST":
        form = InscriptionEtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            etudiant = Etudiant()
            emailForm = form.cleaned_data["email"]
            if len(Etudiant.objects.filter(email = emailForm)) == 0:
                etudiant.nom = form.cleaned_data["nom"]
                etudiant.prenom = form.cleaned_data["prenom"] 
                etudiant.age = form.cleaned_data["age"]           
                etudiant.photo = form.cleaned_data["photo"]            
                etudiant.password = form.cleaned_data["password"]
                etudiant.ecole = form.cleaned_data["ecole"]
                etudiant.description = form.cleaned_data["description"]
                etudiant.email = form.cleaned_data["email"]
                etudiant.save()
            
                sauvegarde = True
                
            else:
                return render(request, 'profils/erreur_inscription.html', locals())
                
    else:
        form = InscriptionEtudiantForm()
    return render(request, 'profils/inscription_etudiant.html', locals())
