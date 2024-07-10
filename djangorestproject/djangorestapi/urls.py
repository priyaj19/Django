from django.urls import include, path

from rest_framework import routers

from djangorestapi.views import PersonViewSet, SpeciesViewSet

from . import views

router = routers.DefaultRouter()
router.register(r"people", PersonViewSet)
router.register(r"species", SpeciesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
