from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SessionSerializer
from .models import Session
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema


"""class SessionGetMethod(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_sessions(self):
        data = SessionSerializer(self.queryset, many=True).data
        return Response(data)

    def get_session(self, pk):
        session_instance = Session.objects.get(id=pk)
        data = session_instance.data
        return Response(data)

    def save_new_session(self, request):
        session_serializer_data = SessionSerializer(data=request.data)
        if session_serializer_data.is_valid():
            session_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response(
                {"message": "Session Added Successfully", "status": status_code}
            )
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(
                {"message": "Please fill in the details", "status": status_code}
            )

    def delete_session(self, request, pk):
        session_data = Session.objects.filter(id=pk)
        if session_data:
            session_data.delete()
            status_code = status.HTTP_204_CREATED
            return Response(f"deleted:" + session_data)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(
                {"message": "Session data not found", "status": status_code}
            )

    def update_session(self, request, pk):
        session_details = Session.objects.get(id=pk)
        session_serializer_data = SessionSerializer(
            session_details, data=request.data, partial=True
        )
        if session_serializer_data.is_valid():
            session_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response(
                {"message": "Session updated successfully", "status": status_code}
            )
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response(
                {"message": "Session data not found", "status": status_code}
            )"""

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
