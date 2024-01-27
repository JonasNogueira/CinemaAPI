from models import Session
from movie.models import Movie
from theater.models import Theater
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):
    movie_name = Movie.name
    theater_number = Theater.number

    class Meta:
        model = Session
        fields = "__all__"
