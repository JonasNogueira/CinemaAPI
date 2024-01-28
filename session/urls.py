from .views import *
from django.urls import path


from django.urls import path
from .views import SessionListCreateView, SessionDetailView

urlpatterns = [
    path("", SessionListCreateView.as_view(), name="session-list-create"),
    path("<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
]
