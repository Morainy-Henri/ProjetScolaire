from django.db import models
from structure.models import Niveau, AnneeScolaire
from eleves.models import Inscription

# Create your models here.
# ==============================
# TARIFICATION ET PAIEMENT
# ==============================
class Tarification(models.Model):
    idTarif = models.AutoField(primary_key=True)
    typePaiement = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    nivRef = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    anneeRef = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.typePaiement} ({self.nivRef})"


class Paiement(models.Model):
    numPaiement = models.AutoField(primary_key=True)
    datePaiement = models.DateField()
    modePaiement = models.CharField(max_length=50)
    montantTotal = models.DecimalField(max_digits=10, decimal_places=2)
    insRef = models.ForeignKey(Inscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"Paiement {self.numPaiement} - {self.insRef}"


class PaiementDetail(models.Model):
    idDetail = models.AutoField(primary_key=True)
    paiementRef = models.ForeignKey(Paiement, on_delete=models.CASCADE)
    tarifRef = models.ForeignKey(Tarification, on_delete=models.CASCADE, null=True, blank=True)
    periode = models.CharField(max_length=50, null=True, blank=True)
    estPaye = models.CharField(max_length=3, choices=[('Oui', 'Oui'), ('Non', 'Non')])

    def __str__(self):
        return f"{self.tarifRef.typePaiement} - {self.periode or 'Unique'}"
