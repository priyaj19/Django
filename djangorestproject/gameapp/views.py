from django.shortcuts import redirect, render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
import requests


class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def index(req):
    return render(req, "index.html")


def instructions(req):
    return render(req, "instructions.html")


def get_game_details(request):
    # Make a request to the API endpoint

    # api_url = "https://378027ioph.execute-api.ap-south-1.amazonaws.com/test/Users?id=ec14dcc2-304-4052-a177-01d68dd6a952"  # Replace with your actual API URL
    api_url = "http://127.0.0.1:8000/gameapp/games/123e4567-e89b-12d3-a456-426614174000/"  # Replace with your actual API URL
    response = requests.get(api_url)
    game_data = response.json()
    print(game_data)
    # Pass the game data to the template
    return render(request, "game_details.html", {"game_data": game_data})
