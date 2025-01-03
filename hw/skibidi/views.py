from rest_framework import generics

from skibidi.models import Game
from skibidi.serializers import GameSerializer

# Create your views here.
class GamesListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer 