from rest_framework import viewsets
from .models import Tuteur, Eleve, Inscription
from .serializers import TuteurSerializer, EleveSerializer, InscriptionSerializer

class TuteurViewSet(viewsets.ModelViewSet):
    queryset = Tuteur.objects.all()
    serializer_class = TuteurSerializer


class EleveViewSet(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer
