from django.test import TestCase

from theater.models import Theater
from theater.serializers import TheaterSerializer


class TheatersListTest(TestCase):
    def setUp(self):
        self.theater1 = {
            "id": 3,
            "number": 101,
            "description": "imax",
        }
        self.theater2 = {
            "id": 2,
            "number": 102,
            "description": "imax",
        }
        self.theater3 = {
            "id": 1,
            "number": 103,
            "description": "imax",
        }
        self.theater5 = {
            "id": 5,
            "number": 104,
            "description": "imax",
        }

    def test_get_theaterlist(self):
        response = self.client.get("/api/theater/")

        self.assertEqual(response.status_code, 200)

        theaters_in_database = Theater.objects.all()

        expected_data = TheaterSerializer(theaters_in_database, many=True).data

        self.assertEqual(response.data, expected_data)
