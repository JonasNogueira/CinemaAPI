from django.test import TestCase
from model_mommy import mommy
from django.test import TestCase


class TheaterTestCase(TestCase):
    def setUp(self) -> None:
        self.theater = mommy.make("Theater")

    def test_str(self):
        self.assertEquals(str(self.theater), f"Theater {self.theater.number}")
