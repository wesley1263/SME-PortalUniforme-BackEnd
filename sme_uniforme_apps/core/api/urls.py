from rest_framework import routers
from django.urls import include, path
from .viewsets.version_viewset import ApiVersion

from sme_uniforme_apps.proponentes.urls import router as proponentes_router

router = routers.DefaultRouter()

router.register('api-version', ApiVersion, basename='Version')

router.registry.extend(proponentes_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
