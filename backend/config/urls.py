from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/eleves/', include('eleves.urls')),
    path('api/discipline/', include('discipline.urls')),
    path('api/emplois/', include('emplois.urls')),
    path('api/enseignement/', include('enseignement.urls')),
    path('api/examens/', include('examens.urls')),
    path('api/paiements/', include('paiements.urls')),
    path('api/structure/', include('structure.urls')),
]
