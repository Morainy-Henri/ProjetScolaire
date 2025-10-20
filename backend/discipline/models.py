from django.db import models
from eleves.models import Inscription

# Create your models here.
# ==============================
# DISCIPLINE
# ==============================
class Sanction(models.Model):
    idSanction = models.AutoField(primary_key=True)
    type_sanction = models.CharField(max_length=100)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    InsRef = models.ForeignKey(Inscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type_sanction} ({self.InsRef})"


class Avertissement(models.Model):
    idAvertissement = models.AutoField(primary_key=True)
    dateAvert = models.DateField()
    description = models.TextField()
    InsRef = models.ForeignKey(Inscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"Avertissement {self.dateAvert} - {self.InsRef}"
