from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^inscription/$', views.inscription),
    url(r'^inscription_etudiant/$', views.inscription_etudiant),
    url(r'^inscription_particulier/$', views.inscription_particulier),
]
