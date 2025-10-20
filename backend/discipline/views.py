from rest_framework import viewsets
from .models import Sanction, Avertissement
from .serializers import SanctionSerializer, AvertissementSerializer

class SanctionViewSet(viewsets.ModelViewSet):
    queryset = Sanction.objects.all()
    serializer_class = SanctionSerializer


class AvertissementViewSet(viewsets.ModelViewSet):
    queryset = Avertissement.objects.all()
    serializer_class = AvertissementSerializer
