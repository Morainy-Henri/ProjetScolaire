from django.db import models
from structure.models import Niveau, Classe

# Create your models here.
# ==============================
# ENSEIGNEMENT
# ==============================
class Enseignant(models.Model):
    idEnseignant = models.AutoField(primary_key=True)
    nomEnseignant = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    adresse = models.CharField(max_length=150)

    def __str__(self):
        return self.nomEnseignant


class Discipline(models.Model):
    idDiscipline = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.libelle


class Matiere(models.Model):
    idMatiere = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)
    disRef = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle


class MatiereNiveau(models.Model):
    nivRef = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    matRef = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeurCoef = models.IntegerField()

    def __str__(self):
        return f"{self.matRef} ({self.nivRef})"


class Enseignement(models.Model):
    idEnseignement = models.AutoField(primary_key=True)
    matRef = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    EnsRef = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.EnsRef} - {self.matRef}"


class EnseignementClasse(models.Model):
    EnsRef = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matRef = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    classeRef = models.ForeignKey(Classe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('EnsRef', 'matRef', 'classeRef')

    def __str__(self):
        return f"{self.EnsRef} - {self.matRef} ({self.classeRef})"
