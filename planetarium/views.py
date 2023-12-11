from rest_framework import viewsets, mixins
from rest_framework.views import APIView

from planetarium.models import AstronomyShow, ShowTheme, PlanetariumDome
from planetarium.serializers import AstronomyShowSerializer, ShowThemeSerializer, PlanetariumDomeSerializer, \
    AstronomyShowListSerializer, AstronomyShowDetailSerializer


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetariumDomeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class AstronomyShowViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AstronomyShowListSerializer

        if self.action == "retrieve":
            return AstronomyShowDetailSerializer

        return AstronomyShowSerializer
