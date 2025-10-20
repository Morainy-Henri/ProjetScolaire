from rest_framework import serializers
from .models import Examen, ClasseExamen, MatiereExamen, Bulletin, Note

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'

class ClasseExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseExamen
        fields = '__all__'

class MatiereExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatiereExamen
        fields = '__all__'

class BulletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bulletin
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
