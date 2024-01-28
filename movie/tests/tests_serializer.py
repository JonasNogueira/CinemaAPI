from django.test import TestCase
from movie.models import Movie
from movie.serializers import MovieSerializer


class MovieSerializerTest(TestCase):
    def test_validate_movie_already_exists(self):
        Movie.objects.create(
            name="Inception", director="Christopher Nolan", duration=150
        )

        data = {"name": "Inception", "director": "Christopher Nolan", "duration": 150}

        serializer = MovieSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn("error", serializer.errors)
        self.assertEqual(serializer.errors["error"][0], "movie_already_exists")

    def test_validate_movie_does_not_exist(self):
        data = {"name": "The Matrix", "director": "Lana Wachowski", "duration": 136}

        serializer = MovieSerializer(data=data)

        self.assertTrue(serializer.is_valid())
