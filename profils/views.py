from django.shortcuts import render, redirect
from django.http import HttpResponse
from profils.forms import InscriptionForm, ConnexionForm
from profils.models import Profil, User, Annonce
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'base.html', locals())


def inscription(request):
    sauvegarde = False
    wrong_email = False
    wrong_username = False
    
    if request.method == "POST":
        form = InscriptionForm(request.POST, request.FILES)
        print("formulaire recu")
        if form.is_valid():
            print("formulaire valide")
            emailForm = form.cleaned_data["email"]
            pseudoForm = form.cleaned_data["pseudo"]
            if (len(User.objects.filter(email = emailForm)) == 0) and (len(User.objects.filter(username = pseudoForm))) == 0:
                print("test ok")
                profil = Profil()
                user = User()
                user.username = form.cleaned_data["pseudo"]
                user.first_name = form.cleaned_data["prenom"]
                user.last_name = form.cleaned_data["nom"] 
                user.email = form.cleaned_data["email"]            
                user.password = form.cleaned_data["password"]
                user.is_staff = False
                user.is_active = True
                user.is_superuser = False
                user.save()
                profil.user = user
                profil.age = form.cleaned_data["age"]           
                profil.photo = form.cleaned_data["photo"]
                print(form.cleaned_data["is_student"])
                profil.is_student = form.cleaned_data["is_student"]
                profil.description = form.cleaned_data["description"]
                if profil.is_student:
                    profil.ecole = form.cleaned_data["école"]
                profil.save()
                
                print("inscription réussie")
                return render(request, 'profils/inscription_reussie.html', locals())
                
            else:
                if len(User.objects.filter(email = emailForm)) != 0:
                    wrong_email = True
                if len(User.objects.filter(username = pseudoForm)) != 0:
                    wrong_username = True
                print("inscription ratée")
                return render(request, 'profils/inscription.html', locals())
                
    else:
        form = InscriptionForm()
    print("envoi formulaire blanc")
    return render(request, 'profils/inscription.html', locals())
    
    
def connexion(request):
    error = False
    
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'profils/connexion.html', locals())
    

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
    

    

    def list_annonce(request):
        annonces = Annonce.objects.all()
        return render(request,'list_annonce.htlm',locals())

    def annonce(resquest,numero) :
        return render(request,'annonce.html',locals())


    
    
    
    
    
    
    
    