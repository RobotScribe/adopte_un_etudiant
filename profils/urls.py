from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^inscription/$', views.inscription),
    url(r'^annonces/$',views.list_annonces),
    url(r'^annonce/(?P<numero>\d+$)',views.annonce)
]
