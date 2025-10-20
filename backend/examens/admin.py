from django.contrib import admin
from .models import (
    Examen,
    ClasseExamen,
    MatiereExamen,
    Bulletin,
    Note
)

@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'anneeRef')
    list_filter = ('anneeRef',)

@admin.register(ClasseExamen)
class ClasseExamenAdmin(admin.ModelAdmin):
    list_display = ('examRef', 'classeRef')

@admin.register(MatiereExamen)
class MatiereExamenAdmin(admin.ModelAdmin):
    list_display = ('examRef', 'matRef')

@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    list_display = ('idBulletin', 'InsRef')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('matRef', 'valeur', 'InsRef')
    list_filter = ('matRef',)
