from rest_framework import serializers
from .models import Tarification, Paiement, PaiementDetail

class TarificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarification
        fields = '__all__'

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'

class PaiementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementDetail
        fields = '__all__'
