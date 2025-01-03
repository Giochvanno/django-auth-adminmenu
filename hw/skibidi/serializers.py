from rest_framework import serializers

from skibidi.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'description', 'author']