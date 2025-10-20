from django.contrib import admin
from .models import Sanction, Avertissement

@admin.register(Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ('type_sanction', 'dateDebut', 'dateFin', 'InsRef')
    list_filter = ('type_sanction',)

@admin.register(Avertissement)
class AvertissementAdmin(admin.ModelAdmin):
    list_display = ('dateAvert', 'description', 'InsRef')
