from django.contrib import admin
from .models import Cycle, Niveau, AnneeScolaire, Classe

@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('libelle',)

@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'cycleRef')

@admin.register(AnneeScolaire)
class AnneeScolaireAdmin(admin.ModelAdmin):
    list_display = ('annee',)

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'nivRef', 'anneeRef')
