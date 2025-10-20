from django.contrib import admin
from .models import (
    Enseignant,
    Discipline,
    Matiere,
    MatiereNiveau,
    Enseignement,
    EnseignementClasse
)

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nomEnseignant', 'contact', 'adresse')

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description')

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'disRef')
    list_filter = ('disRef',)

@admin.register(MatiereNiveau)
class MatiereNiveauAdmin(admin.ModelAdmin):
    list_display = ('matRef', 'nivRef', 'valeurCoef')
    list_filter = ('nivRef',)

@admin.register(Enseignement)
class EnseignementAdmin(admin.ModelAdmin):
    list_display = ('EnsRef', 'matRef')

@admin.register(EnseignementClasse)
class EnseignementClasseAdmin(admin.ModelAdmin):
    list_display = ('EnsRef', 'matRef', 'classeRef')
    list_filter = ('classeRef',)
