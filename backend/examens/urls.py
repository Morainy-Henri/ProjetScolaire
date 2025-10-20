from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExamenViewSet, ClasseExamenViewSet, MatiereExamenViewSet,
    BulletinViewSet, NoteViewSet
)

router = DefaultRouter()
router.register('examens', ExamenViewSet)
router.register('classe-examens', ClasseExamenViewSet)
router.register('matiere-examens', MatiereExamenViewSet)
router.register('bulletins', BulletinViewSet)
router.register('notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
