from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate(self, data):
        """
        Verifica se já existe um filme com as mesmas informações.
        """
        existing_movie = Movie.objects.filter(
            name=data["name"], director=data["director"], duration=data["duration"]
        )

        if existing_movie.exists():
            raise serializers.ValidationError({"error": "movie_already_exists"})

        return data
