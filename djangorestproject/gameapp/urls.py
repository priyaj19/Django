from django.urls import path
from .views import GameDetailView
from . import views as v

urlpatterns = [
    path("", v.index, name="index"),
    path("instructions/", v.instructions, name="instructions"),
    path("games/<uuid:pk>/", GameDetailView.as_view(), name="game-detail"),
    path("get_game_details/", v.get_game_details, name="get_game_details"),
]
