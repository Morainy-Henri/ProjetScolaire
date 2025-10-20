from django.db import models
from structure.models import Classe, AnneeScolaire
from enseignement.models import Matiere
from eleves.models import Inscription

# Create your models here.
# ==============================
# EXAMENS ET NOTES
# ==============================
class Examen(models.Model):
    idExamen = models.AutoField(primary_key=True)
    anneeRef = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class ClasseExamen(models.Model):
    classeRef = models.ForeignKey(Classe, on_delete=models.CASCADE)
    examRef = models.ForeignKey(Examen, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('classeRef', 'examRef')

    def __str__(self):
        return f"{self.examRef} ({self.classeRef})"


class MatiereExamen(models.Model):
    matRef = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    examRef = models.ForeignKey(Examen, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('matRef', 'examRef')

    def __str__(self):
        return f"{self.matRef} ({self.examRef})"


class Bulletin(models.Model):
    idBulletin = models.AutoField(primary_key=True)
    InsRef = models.ForeignKey(Inscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bulletin - {self.InsRef}"


class Note(models.Model):
    idNote = models.AutoField(primary_key=True)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)
    appreciation = models.TextField()
    InsRef = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    matRef = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.matRef} - {self.valeur}"

