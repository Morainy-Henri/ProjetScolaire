from django.db import models
from structure.models import Classe

# Create your models here.
# ==============================
# ELEVES ET TUTEURS
# ==============================
class Tuteur(models.Model):
    idTuteur = models.AutoField(primary_key=True)
    tuteur = models.CharField(max_length=100)
    professionTuteur = models.CharField(max_length=100)
    contactTuteur = models.CharField(max_length=20)

    def __str__(self):
        return self.tuteur


class Eleve(models.Model):
    idEleve = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dateNaissance = models.DateField()
    lieuNaissance = models.CharField(max_length=100)
    tuteurRef = models.ForeignKey(Tuteur, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.matricule})"


class Inscription(models.Model):
    idInscription = models.AutoField(primary_key=True)
    dateInscription = models.DateField()
    statut = models.CharField(max_length=50)
    classeRef = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleveRef = models.ForeignKey(Eleve, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.eleveRef} - {self.classeRef}"
