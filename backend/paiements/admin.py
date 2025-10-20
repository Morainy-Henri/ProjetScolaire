from django.contrib import admin
from .models import Tarification, Paiement, PaiementDetail

@admin.register(Tarification)
class TarificationAdmin(admin.ModelAdmin):
    list_display = ('typePaiement', 'montant', 'nivRef', 'anneeRef')
    list_filter = ('nivRef', 'anneeRef')

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('numPaiement', 'datePaiement', 'modePaiement', 'montantTotal', 'insRef')
    list_filter = ('datePaiement', 'modePaiement')

@admin.register(PaiementDetail)
class PaiementDetailAdmin(admin.ModelAdmin):
    list_display = ('paiementRef', 'tarifRef', 'periode', 'estPaye')
    list_filter = ('estPaye',)
