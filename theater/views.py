from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TheaterSerializer
from .models import Theater


class TheatersList(ListCreateAPIView):
    serializer_class = TheaterSerializer
    queryset = Theater.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class TheaterDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TheaterSerializer
    queryset = Theater.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()
