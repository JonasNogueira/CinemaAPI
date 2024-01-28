from django.test import TestCase
from theater.models import Theater
from theater.serializers import TheaterSerializer


class TheaterSerializerTest(TestCase):
    def test_validate_number_theater_already_exists(self):
        Theater.objects.create(number=1, description="Some description")

        data = {"number": 1, "description": "Another description"}

        serializer = TheaterSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn("number", serializer.errors)
        self.assertIn("error", serializer.errors["number"])
        self.assertEqual(serializer.errors["number"]["error"][0], "t")
