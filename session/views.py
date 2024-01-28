from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SessionSerializer
from .models import Session


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Session
from .serializers import SessionSerializer, SessionDetailSerializer


class SessionListCreateView(ListCreateAPIView):
    queryset = Session.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SessionDetailSerializer
        return SessionSerializer


class SessionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
