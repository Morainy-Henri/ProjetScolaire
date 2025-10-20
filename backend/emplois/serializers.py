from rest_framework import serializers
from .models import EmploisDuTemps, Jour, Creneau, DisciplineCreneau, Sceance

class EmploisDuTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploisDuTemps
        fields = '__all__'

class JourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jour
        fields = '__all__'

class CreneauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creneau
        fields = '__all__'

class DisciplineCreneauSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineCreneau
        fields = '__all__'

class SceanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sceance
        fields = '__all__'
 