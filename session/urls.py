from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

"""session_router = DefaultRouter()
session_router.register(r"", SessionGetMethod, basename="session")

urlpatterns = [
    path("", include(session_router.urls)),
]"""
from django.urls import path
from .views import SessionListCreateView, SessionDetailView

urlpatterns = [
    path("", SessionListCreateView.as_view(), name="session-list-create"),
    path("<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
]
