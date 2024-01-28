from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
from .models import Movie


class MoviesList(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()
