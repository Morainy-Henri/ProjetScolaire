from django.contrib import admin
from .models import EmploisDuTemps, Jour, Creneau, DisciplineCreneau, Sceance

@admin.register(EmploisDuTemps)
class EmploisDuTempsAdmin(admin.ModelAdmin):
    list_display = ('idEDT', 'classeRef')

@admin.register(Jour)
class JourAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'edtRef')

@admin.register(Creneau)
class CreneauAdmin(admin.ModelAdmin):
    list_display = ('jourRef', 'heureDebut', 'heureFin')

@admin.register(DisciplineCreneau)
class DisciplineCreneauAdmin(admin.ModelAdmin):
    list_display = ('disRef', 'creneauRef')

@admin.register(Sceance)
class SceanceAdmin(admin.ModelAdmin):
    list_display = ('creneauRef', 'EnsRef')
