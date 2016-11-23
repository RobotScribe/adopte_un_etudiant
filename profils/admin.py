from django.contrib import admin
from profils.models import Profil

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'is_student',)
    list_filter = ('is_student',) 
    search_fields = ('user',)

admin.site.register(Profil, ProfilAdmin)
