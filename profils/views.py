from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from profils.forms import *
from profils.models import *
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', locals())
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
    if not(request.user.is_authenticated):
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
                    return redirect(home)
                else: # sinon une erreur sera affichée
                    error = True
                    
        else:
            form = ConnexionForm()
        return render(request, 'profils/connexion.html', locals())
    else:
        return redirect('/')    
    


@login_required(login_url = '/connexion/')
def deconnexion(request):
    logout(request)
    return redirect(reverse(home))
    

    

def list_annonces(request):
    annonces = Annonce.objects.filter(etat="a_faire")
    return render(request,'profils/list_annonces.html',locals())

def annonce(request,numero) :
    annonce = Annonce.objects.get(numero=numero)
    Bool = annonce.distance_max != 0
    return render(request,'profils/annonce.html',locals())


@login_required(login_url = '/connexion/')   
def annonce_perso(request,numero):
    annonce = Annonce.objects.get(numero=numero)
    user_annonceur = User.objects.get(username=annonce.annonceur)
    if ((annonce.annonceur == request.user.username) or(annonce.postulant == request.user.username)):
        Bool = annonce.distance_max != 0
        return render(request,'profils/annonce_perso.html',locals())
    else:
        raise Http404
        
        
@login_required(login_url = '/connexion/')   
def modifier_annonce(request,numero):
    annonce = Annonce.objects.get(numero=numero)
    if annonce.annonceur == request.user.username:
        wrong_password = False
        if request.method == "POST":
            form = ModifierAnnonceForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                if authenticate(username=request.user.username, password=password):
                    annonce.titre = form.cleaned_data["titre"]
                    annonce.annonce = form.cleaned_data["annonce"]
                    annonce.prix = form.cleaned_data["prix"]
                    annonce.lieux = form.cleaned_data["lieux"]
                    annonce.distance_max = form.cleaned_data["distance_max"]
                    annonce.save()
                    return redirect('/voir_annonces_perso/a_faire')
                else:
                    wrong_password = True
                    return render(request, 'profils/modifier_annonce.html', locals())
        else:
            form = ModifierAnnonceForm()
            return render(request, 'profils/modifier_annonce.html', locals())
    else:
        raise Http404
        
        
@login_required(login_url = '/connexion/')   
def supprimer_annonce(request,numero):
    annonce = Annonce.objects.get(numero=numero)
    if annonce.annonceur == request.user.username:
        wrong_password = False
        if request.method == "POST":
            form = DemanderPasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                if authenticate(username=request.user.username, password=password):
                    annonce.delete()
                    return redirect('/voir_annonces_perso/a_faire')
                else:
                    wrong_password = True
                    return render(request, 'profils/supprimer_annonce.html', locals())
        else:
            form = DemanderPasswordForm()
            return render(request, 'profils/supprimer_annonce.html', locals())
    else:
        raise Http404
        
    
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
                print(annonce.titre)
                #annonce.boulot=form.cleaned_data["boulot"]
                annonce.annonce=form.cleaned_data["annonce"]
                print(annonce.annonce)
                annonce.prix=form.cleaned_data["prix"]
                annonce.lieux = form.cleaned_data["lieux"]
                annonce.distance_max=form.cleaned_data["distance_max"]
                annonce.etat = "a_faire"
                print(request.user)
                annonce.annonceur = request.user.username
                
                list_annonces = Annonce.objects.all()# a changer #
                list_num = []
                for annonce_deja_creee in list_annonces:
                    list_num.append(annonce_deja_creee.numero)
                
                if len(list_num) == 0:
                    annonce.numero = 1
                else:
                    annonce.numero = max(list_num) + 1
                
                annonce.save()
                return render(request, 'profils/annonce_reussie.html', locals())
                      
        else:
            
            form = AnnonceForm()
            print('creation du formulaire')

        return render(request, 'profils/proposer_annonce.html', locals())
    
    else :
        return redirect(connexion)
        
        
@login_required(login_url = '/connexion/')           
def postuler_annonce(request, numero):
    profil = Profil.objects.get(user=request.user)
    annonce = Annonce.objects.get(numero=numero)
    if profil.is_student:#On vérifie que le postulant est bien étudiant
        if annonce.annonceur != profil.user.username:#On vérifie qu'il ne postule pas à sa propre annonce
            form = PostulerAnnonceForm(request.POST)
            if request.method == "POST":
                if form.is_valid():
                    annonce.postulant = profil.user.username
                    annonce.message_postulant = form.cleaned_data["Commentaires"]
                    annonce.etat = "en_cours"
                    annonce.save()
                    return redirect('/voir_annonces_perso/en_cours')
            else:
                form = PostulerAnnonceForm()
                return render(request, 'profils/postuler_annonce.html', locals())
        else:
            raise Http404          
    else:
        raise Http404
                
    
def test(request):
    return render(request, 'profils/test.html')
    
def profil(request):
    if request.user.is_authenticated:
        profil = Profil.objects.get(user = request.user)
        return render(request, 'profils/voir_profil.html', locals())
    else:
        return redirect(connexion)
        
def modifier_profil(request):
    print("ok0")
    if request.user.is_authenticated:
        profil = Profil.objects.get(user = request.user)
        wrong_username = False
        wrong_password = False
        
        print("ok1")
        
        if request.method == "POST":
            form = ModifierProfilForm(request.POST)
            
            if form.is_valid():
                password = form.cleaned_data["password"]
                if authenticate(username=request.user.username, password=password):                
                    new_username = form.cleaned_data["pseudo"]
                    if (len(User.objects.filter(username = new_username)) == 0) or (new_username == request.user.username):
                        user = profil.user
                        user.username = new_username
                        new_password = form.cleaned_data["new_password"]
                        user.set_password(new_password)
                        user.save() 
                        profil.user = user
                        profil.photo = form.cleaned_data["photo"]
                        profil.description = form.cleaned_data["description"]
                        profil.is_student = form.cleaned_data["is_student"]
                        if profil.is_student:
                            profil.ecole = form.cleaned_data["école"]
                            
                           
                        profil.save()
                        
                        authenticate(username=user.username, password=new_password)
                        login(request, user)
                        
                        
                        return redirect('/profil/')
                        
                    else:
                        wrong_username = True
                        return render(request, 'profils/modifier_profil.html', locals())
                else:
                    wrong_password = True
                    return render(request, 'profils/modifier_profil.html', locals())
        else:
            form = ModifierProfilForm()
            return render(request, 'profils/modifier_profil.html', locals())
        
    else:
        return redirect(connexion)
        
        

def voir_annonces_afaire(request, etat):
    print("ok1")
    profil = Profil.objects.get(user = request.user)
    pseudo = request.user.username
    print(pseudo)
    if etat == "a_faire":
        annonces = Annonce.objects.filter(etat="a_faire", annonceur = pseudo)
        return render(request,'profils/list_annonces_perso.html',locals())
    if etat == "en_cours":
        print("ok2encours")
        annonces_particulier = Annonce.objects.filter(etat="en_cours", annonceur = pseudo)
        annonces_postulees = Annonce.objects.filter(etat="en_cours", postulant = pseudo)
        print(len(annonces_postulees))
        annonces_etudiant = Annonce.objects.filter(etat="en_cours", etudiant = pseudo)      
        return render(request,'profils/list_annonces_perso.html',locals())
    if etat == "fait":
        annonces_particulier = Annonce.objects.filter(etat="fait", annonceur = pseudo)
        annonces_etudiant = Annonce.objects.filter(etat="fait", etudiant = pseudo)  
        return render(request,'profils/list_annonces_perso.html',locals())
        
        

@login_required(login_url = '/connexion/')          
def annuler_annonce(request, numero):
    annonce = Annonce.objects.get(numero=numero)
    if ((annonce.postulant == request.user.username) or (annonce.annonceur == request.user.username)):
        wrong_password = False
        if request.method == "POST":
            form = DemanderPasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                if authenticate(username=request.user.username, password=password):
                    annonce.postulant = None
                    annonce.etudiant = ''
                    annonce.etat = "a_faire"
                    annonce.save()
                    return redirect('/voir_annonces_perso/en_cours')
                else:
                    wrong_password = True
                    return render(request, 'profils/annuler_annonce_etudiant.html', locals())
        else:
            form = DemanderPasswordForm()
            return render(request, 'profils/annuler_annonce_etudiant.html', locals())
    else:
        raise Http404
        
def accepter_annonce(request, numero):
    pass
    
def refuser_annonce(request, numero):
    pass
    
def annonce_effectuee(request, numero):
    pass
        
























    

    
    
    
    
    
