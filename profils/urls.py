from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^inscription/$', views.inscription),
    url(r'^connexion/$', views.connexion, name = 'connexion'),
    url(r'^deconnexion/$', views.deconnexion, name = 'deconnexion'),
    url(r'^annonces/$',views.list_annonces),
    url(r'^annonce/(?P<numero>\d+$)',views.annonce, name= 'lire_annonce'),
    url(r'^proposer_annonce/$',views.proposer_annonce),
    url(r'^postuler_annonce/(?P<numero>\d+$)',views.postuler_annonce, name = 'postuler_annonce'),
    url(r'^profil/(?P<client>\d+$)',views.profil_client, name = 'voir_client')

]
