from rest_framework import viewsets
from .models import EmploisDuTemps, Jour, Creneau, DisciplineCreneau, Sceance
from .serializers import (
    EmploisDuTempsSerializer, JourSerializer, CreneauSerializer,
    DisciplineCreneauSerializer, SceanceSerializer
)

class EmploisDuTempsViewSet(viewsets.ModelViewSet):
    queryset = EmploisDuTemps.objects.all()
    serializer_class = EmploisDuTempsSerializer

class JourViewSet(viewsets.ModelViewSet):
    queryset = Jour.objects.all()
    serializer_class = JourSerializer

class CreneauViewSet(viewsets.ModelViewSet):
    queryset = Creneau.objects.all()
    serializer_class = CreneauSerializer

class DisciplineCreneauViewSet(viewsets.ModelViewSet):
    queryset = DisciplineCreneau.objects.all()
    serializer_class = DisciplineCreneauSerializer

class SceanceViewSet(viewsets.ModelViewSet):
    queryset = Sceance.objects.all()
    serializer_class = SceanceSerializer
