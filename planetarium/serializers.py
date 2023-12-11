from rest_framework import serializers

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome, ShowSession
)


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ["id", "name"]


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = [
            "id",
            "title",
            "show_themes"
        ]


class AstronomyShowListSerializer(serializers.ModelSerializer):
    show_themes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = AstronomyShow
        fields = ["id", "title", "show_themes",]


class AstronomyShowDetailSerializer(AstronomyShowSerializer):
    show_themes = AstronomyShowListSerializer(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = [
            "id",
            "title",
            "description",
            "show_themes",
        ]


class ShowSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = [
            "id",
            "show_time",
            "astronomy_show",
            "planetarium_dome",
        ]


class ShowSessionListSerializer(serializers.ModelSerializer):
    astronomy_show_title = serializers.CharField(
        source="astronomy_show.title",
        read_only=True,
    )
    planetarium_dome_name = serializers.CharField(
        source="planetarium_dome.name",
        read_only=True,
    )
    planetarium_dome_capacity = serializers.IntegerField(
        source="planetarium_dome.capacity",
        read_only=True,
    )

    class Meta:
        model = ShowSession
        fields = [
            "id",
            "show_time",
            "astronomy_show_title",
            "planetarium_dome_name",
            "planetarium_dome_capacity",
        ]