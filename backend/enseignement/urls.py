from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EnseignantViewSet, DisciplineViewSet, MatiereViewSet,
    MatiereNiveauViewSet, EnseignementViewSet, EnseignementClasseViewSet
)

router = DefaultRouter()
router.register('enseignants', EnseignantViewSet)
router.register('disciplines', DisciplineViewSet)
router.register('matieres', MatiereViewSet)
router.register('matiere-niveaux', MatiereNiveauViewSet)
router.register('enseignements', EnseignementViewSet)
router.register('enseignement-classes', EnseignementClasseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
