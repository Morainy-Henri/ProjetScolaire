from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SanctionViewSet, AvertissementViewSet

router = DefaultRouter()
router.register('sanctions', SanctionViewSet)
router.register('avertissements', AvertissementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
