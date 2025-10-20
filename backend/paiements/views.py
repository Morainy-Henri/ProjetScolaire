from rest_framework import viewsets
from .models import Tarification, Paiement, PaiementDetail
from .serializers import TarificationSerializer, PaiementSerializer, PaiementDetailSerializer

class TarificationViewSet(viewsets.ModelViewSet):
    queryset = Tarification.objects.all()
    serializer_class = TarificationSerializer

class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class PaiementDetailViewSet(viewsets.ModelViewSet):
    queryset = PaiementDetail.objects.all()
    serializer_class = PaiementDetailSerializer
