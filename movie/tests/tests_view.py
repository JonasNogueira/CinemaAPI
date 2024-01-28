from django.test import TestCase

from movie.models import Movie
from movie.serializers import MovieSerializer


from django.test import TestCase


class MoviesListTest(TestCase):
    def setUp(self):
        self.movie1 = {
            "id": 3,
            "name": "Inception",
            "director": "Christopher Nolan",
            "duration": 150,
        }
        self.movie2 = {
            "id": 2,
            "name": "The Matrix",
            "director": "Lana Wachowski",
            "duration": 136,
        }
        self.movie3 = {
            "id": 1,
            "name": "The Shawshank Redemption",
            "director": "Frank Darabont",
            "duration": 142,
        }
        self.movie5 = {
            "id": 5,
            "name": "Django Unchained",
            "director": "Quentin Tarantino",
            "duration": 165,
        }

    def test_create_movie(self):
        response = self.client.post("/api/movie/", data=self.movie1)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.data, MovieSerializer(self.movie1).data)

    def test_get_movielist(self):
        response = self.client.get("/api/movie/")

        self.assertEqual(response.status_code, 200)

        movies_in_database = Movie.objects.all()

        expected_data = MovieSerializer(movies_in_database, many=True).data

        self.assertEqual(response.data, expected_data)
