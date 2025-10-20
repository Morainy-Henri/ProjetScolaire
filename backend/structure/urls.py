from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CycleViewSet, NiveauViewSet, AnneeScolaireViewSet, ClasseViewSet

router = DefaultRouter()
router.register('cycles', CycleViewSet)
router.register('niveaux', NiveauViewSet)
router.register('annees-scolaires', AnneeScolaireViewSet)
router.register('classes', ClasseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
