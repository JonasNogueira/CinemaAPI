from .models import Session

from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class SessionDetailSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source="movie.name", read_only=True)
    theater_number = serializers.IntegerField(source="theater.number", read_only=True)

    class Meta:
        model = Session
        fields = ["id", "movie_name", "theater_number", "start_time"]
