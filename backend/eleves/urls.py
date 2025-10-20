from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TuteurViewSet, EleveViewSet, InscriptionViewSet

router = DefaultRouter()
router.register('tuteurs', TuteurViewSet)
router.register('eleves', EleveViewSet)
router.register('inscriptions', InscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
