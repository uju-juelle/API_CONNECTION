from django.urls import path
from .views import *


urlpatterns = [
    path("generate-movies/", generate_movies.as_view(), name="moivies"),
    # path("", Homepage.as_view(), name="home"),
    # path("<int:id>/", detailpage.as_view(), name="detail"),
]