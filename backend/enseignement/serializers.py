from rest_framework import serializers
from .models import Enseignant, Discipline, Matiere, MatiereNiveau, Enseignement, EnseignementClasse

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = '__all__'

class MatiereNiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatiereNiveau
        fields = '__all__'

class EnseignementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignement
        fields = '__all__'

class EnseignementClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnseignementClasse
        fields = '__all__'
