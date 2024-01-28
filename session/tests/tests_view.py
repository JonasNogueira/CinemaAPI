from django.test import TestCase

from session.models import Session
from session.serializers import SessionDetailSerializer

from movie.models import Movie
from theater.models import Theater


class SessionListCreateViewTest(TestCase):
    def setUp(self):
        # Supondo que você já tenha instâncias de Movie e Theater no banco de dados
        self.movie = Movie.objects.create(
            name="Inception", director="Christopher Nolan", duration=150
        )
        self.theater = Theater.objects.create(number=101, description="Large theater")

        self.session1 = {
            "id": 1,
            "movie": self.movie.id,
            "theater": self.theater.id,
            "start_time": "2024-01-27T12:00:00Z",
        }

        self.session2 = {
            "id": 2,
            "movie": self.movie.id,
            "theater": self.theater.id,
            "start_time": "2024-01-27T15:00:00Z",
        }

    def test_get_sessionlist(self):
        response = self.client.get("/api/session/")

        self.assertEqual(response.status_code, 200)

        sessions_in_database = Session.objects.all()

        expected_data = SessionDetailSerializer(sessions_in_database, many=True).data

        self.assertEqual(response.data, expected_data)
