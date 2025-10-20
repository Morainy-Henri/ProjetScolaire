from django.contrib import admin
from .models import Tuteur, Eleve, Inscription
from structure.models import Classe  # pour info dans admin si tu veux des filtres

@admin.register(Tuteur)
class TuteurAdmin(admin.ModelAdmin):
    list_display = ('tuteur', 'professionTuteur', 'contactTuteur')

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'dateNaissance', 'lieuNaissance', 'tuteurRef')
    search_fields = ('matricule', 'nom', 'prenom')

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('eleveRef', 'classeRef', 'dateInscription', 'statut')
    list_filter = ('classeRef', 'statut')
