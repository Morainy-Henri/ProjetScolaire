from django.db import models
from structure.models import Classe
from enseignement.models import Discipline, Enseignant

# Create your models here.
# ==============================
# EMPLOIS DU TEMPS
# ==============================
class EmploisDuTemps(models.Model):
    idEDT = models.AutoField(primary_key=True)
    classeRef = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return f"EDT {self.classeRef}"


class Jour(models.Model):
    libelle = models.CharField(max_length=20, primary_key=True)
    edtRef = models.ForeignKey(EmploisDuTemps, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle


class Creneau(models.Model):
    idCreneau = models.AutoField(primary_key=True)
    jourRef = models.ForeignKey(Jour, on_delete=models.CASCADE)
    heureDebut = models.TimeField()
    heureFin = models.TimeField()

    def __str__(self):
        return f"{self.jourRef} {self.heureDebut}-{self.heureFin}"


class DisciplineCreneau(models.Model):
    disRef = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    creneauRef = models.ForeignKey(Creneau, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.disRef} ({self.creneauRef})"


class Sceance(models.Model):
    idSceance = models.AutoField(primary_key=True)
    creneauRef = models.ForeignKey(Creneau, on_delete=models.CASCADE)
    EnsRef = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.creneauRef} - {self.EnsRef}"
