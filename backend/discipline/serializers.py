from rest_framework import serializers
from .models import Sanction, Avertissement

class SanctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanction
        fields = '__all__'


class AvertissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avertissement
        fields = '__all__'
