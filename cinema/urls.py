from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from movie.urls import *
from theater.urls import *
from session.urls import *


schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        default_version="v1",
        description="API for managing movies, theaters, and sessions in a cinema",
        contact=openapi.Contact(email="jonas.nogueira@aluno.uece.br"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/movie/", include("movie.urls")),
    path("api/theater/", include("theater.urls")),
    path("api/session/", include("session.urls")),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
