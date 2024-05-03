from django.contrib import admin

# Register your models here.
from . models import Eleve, Livre


class EleveAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'quantite', 'eleve')


admin.site.register(Eleve, EleveAdmin)
admin.site.register(Livre, LivreAdmin)
