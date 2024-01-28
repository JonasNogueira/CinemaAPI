from django.urls import path
from .views import TheatersList, TheaterDetailAPIView

urlpatterns = [
    path("", TheatersList.as_view()),
    path("<int:id>", TheaterDetailAPIView.as_view()),
]
