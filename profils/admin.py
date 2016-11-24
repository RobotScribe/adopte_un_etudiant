from django.contrib import admin
from profils.models import Profil, Annonce


class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'is_student',)
    list_filter = ('is_student',) 
    search_fields = ('user',)
    
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'annonceur', 'date', 'prix', 'numero')
    list_filter = ('date', 'annonceur',)
    search_fields = ('titre', 'annonce',) 


admin.site.register(Profil, ProfilAdmin)
admin.site.register(Annonce, AnnonceAdmin)
