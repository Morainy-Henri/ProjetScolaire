from rest_framework import viewsets
from .models import Examen, ClasseExamen, MatiereExamen, Bulletin, Note
from .serializers import (
    ExamenSerializer, ClasseExamenSerializer, MatiereExamenSerializer,
    BulletinSerializer, NoteSerializer
)

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class ClasseExamenViewSet(viewsets.ModelViewSet):
    queryset = ClasseExamen.objects.all()
    serializer_class = ClasseExamenSerializer

class MatiereExamenViewSet(viewsets.ModelViewSet):
    queryset = MatiereExamen.objects.all()
    serializer_class = MatiereExamenSerializer

class BulletinViewSet(viewsets.ModelViewSet):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
