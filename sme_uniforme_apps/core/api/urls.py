from rest_framework import routers
from django.urls import include, path
from .viewsets.version_viewset import ApiVersion

router = routers.DefaultRouter()

router.register('api-version', ApiVersion, basename='Version')

urlpatterns = [
    path('', include(router.urls))
]
