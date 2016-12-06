from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^inscription/$', views.inscription),
    url(r'^connexion/$', views.connexion, name = 'connexion'),
    url(r'^deconnexion/$', views.deconnexion, name = 'deconnexion'),
    url(r'^annonces/$',views.list_annonces),
    url(r'^annonce/(?P<numero>\d+$)',views.annonce, name= 'lire_annonce'),
    url(r'^proposer_annonce/$',views.proposer_annonce),
    url(r'^postuler_annonce/(?P<numero>\d+$)',views.postuler_annonce, name = 'postuler_annonce'),
    url(r'^test/?$', views.test, name = 'test'),
    url(r'^profil/?$', views.profil, name = 'profil'),
    url(r'^modifier_profil/?$', views.modifier_profil),
    url(r'^voir_annonces_perso/(?P<etat>\w+$)', views.voir_annonces_perso),
    url(r'^annonce_perso/(?P<numero>\d+$)',views.annonce_perso, name= 'lire_annonce_perso'),
    url(r'^modifier_annonce/(?P<numero>\d+$)',views.modifier_annonce, name= 'modifier_annonce'),
    url(r'^supprimer_annonce/(?P<numero>\d+$)',views.supprimer_annonce, name= 'supprimer_annonce'),
    url(r'^annuler_annonce/(?P<numero>\d+$)', views.annuler_annonce, name = 'annuler_annonce'),
    url(r'^accepter_annonce/(?P<numero>\d+$)', views.accepter_annonce, name = 'accepter_annonce'),
    url(r'^refuser_annonce/(?P<numero>\d+$)', views.refuser_annonce, name = 'refuser_annonce'),
    url(r'^annonce_effectuee/(?P<numero>\d+$)', views.annonce_effectuee, name = 'annonce_effectuee'),
]
