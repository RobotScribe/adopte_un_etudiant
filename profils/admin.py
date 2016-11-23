from django.contrib import admin
from profils.models import Profil

class ProfilAdmin(admin.ModelAdmin):
    #list_display = ('user.username', 'user.email', 'is_student', 'user.last-login', 'user.date_joines')
    list_filter = ('is_student',)#,'is_active') 
    #search_fields = ('user.username', 'user.first_name', 'user.last_name', 'user.email')

admin.site.register(Profil, ProfilAdmin)
