from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmploisDuTempsViewSet, JourViewSet, CreneauViewSet,
    DisciplineCreneauViewSet, SceanceViewSet
)

router = DefaultRouter()
router.register('edt', EmploisDuTempsViewSet)
router.register('jours', JourViewSet)
router.register('creneaux', CreneauViewSet)
router.register('discipline-creneaux', DisciplineCreneauViewSet)
router.register('sceances', SceanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
