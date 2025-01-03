from django.urls import path

from skibidi.views import GamesListView

urlpatterns = [
    path("", GamesListView.as_view(), name="games list")
]