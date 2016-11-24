from django.shortcuts import render, redirect
from django.http import HttpResponse
from profils.forms import InscriptionForm, ConnexionForm, AnnonceForm
from profils.models import Profil, User, Annonce
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'base.html', locals())


def inscription(request):
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
                password = form.cleaned_data["password"]
                user.set_password(password)
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
                
                return redirect(reverse(connexion), False)
                
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
            print(user)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'profils/connexion.html', locals())
    

def deconnexion(request):
    logout(request)
    return redirect(reverse(home))
    

    

def list_annonces(request):
    annonces = Annonce.objects.all()
    return render(request,'profils/list_annonce.html',locals())

def annonce(resquest,numero) :
    annonce = get_object_or_404(Annonce, numero=numero)
    return render(request,'profils/annonce.html',locals())
    
def proposer_annonce(request):
    if request.user.is_authenticated:
        print('authentification réussie')

        if request.method == "POST":
            form = AnnonceForm(request.POST)
            print("annonce reçue")
            if form.is_valid():
                annonce = Annonce()
                print("formulaire valide")
                annonce.titre=form.cleaned_data["titre"]
                annonce.boulot=form.cleaned_data["boulot"]
                annonce.annonce=form.cleaned_data["annonce"]
                annonce.prix=form.annonce.cleaned_data["prix"]
                annonce.lieux = form.annonce.cleaned_data["lieux"]
                annonce.distance_max=form.annonce.cleaned_data["distance_max"]
                annonce.save()
                return render(request, 'profils/annonce_reussie.html', locals())
                      
        else:
            
            form = AnnonceForm()
            print('creation du formulaire')

        return render(request, 'profils/proposer_annonce.html', locals())
    
    else :
        return redirect(connexion)
    
    
    
    
    
