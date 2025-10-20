from django.db import models

# Create your models here.
# ==============================
# STRUCTURE SCOLAIRE
# ==============================
class Cycle(models.Model):
    libelle = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.libelle


class Niveau(models.Model):
    libelle = models.CharField(max_length=100, primary_key=True)
    cycleRef = models.ForeignKey(Cycle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.libelle} ({self.cycleRef})"


class AnneeScolaire(models.Model):
    idAnnee = models.AutoField(primary_key=True)
    annee = models.CharField(max_length=9)  # ex: '2025-2026'

    def __str__(self):
        return self.annee


class Classe(models.Model):
    idClasse = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)
    nivRef = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    anneeRef = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.libelle} ({self.nivRef})"
