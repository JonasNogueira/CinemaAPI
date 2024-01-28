import datetime
from django.test import TestCase
from model_mommy import mommy
from django.test import TestCase
from model_mommy import mommy
from session.models import Session
from movie.models import Movie
from theater.models import Theater
from datetime import datetime


class SessionTestCase(TestCase):
    def setUp(self):
        self.movie = mommy.make(Movie)
        self.theater = mommy.make(Theater)
        self.session = mommy.make(
            Session, movie=self.movie, theater=self.theater, start_time=datetime.now()
        )

    def test_str(self):
        expected_str = f"{self.movie} at {self.theater} - {self.session.start_time}"
        self.assertEqual(str(self.session), expected_str)
