from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TarificationViewSet, PaiementViewSet, PaiementDetailViewSet

router = DefaultRouter()
router.register('tarifications', TarificationViewSet)
router.register('paiements', PaiementViewSet)
router.register('paiement-details', PaiementDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
