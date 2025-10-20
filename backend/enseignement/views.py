from rest_framework import viewsets
from .models import Enseignant, Discipline, Matiere, MatiereNiveau, Enseignement, EnseignementClasse
from .serializers import (
    EnseignantSerializer, DisciplineSerializer, MatiereSerializer,
    MatiereNiveauSerializer, EnseignementSerializer, EnseignementClasseSerializer
)

class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer

class MatiereNiveauViewSet(viewsets.ModelViewSet):
    queryset = MatiereNiveau.objects.all()
    serializer_class = MatiereNiveauSerializer

class EnseignementViewSet(viewsets.ModelViewSet):
    queryset = Enseignement.objects.all()
    serializer_class = EnseignementSerializer

class EnseignementClasseViewSet(viewsets.ModelViewSet):
    queryset = EnseignementClasse.objects.all()
    serializer_class = EnseignementClasseSerializer
