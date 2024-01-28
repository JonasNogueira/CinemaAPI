from django.test import TestCase
from model_mommy import mommy
from django.test import TestCase
from model_mommy import mommy


class MovieTestCase(TestCase):
    def setUp(self) -> None:
        self.movie = mommy.make("Movie")

    def test_str(self):
        self.assertEquals(str(self.movie), self.movie.name)
