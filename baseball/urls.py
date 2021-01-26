from django.urls import path

from . import views

app_name = "baseball"
urlpatterns = [
    path("", views.baseball_home, name="baseball-home"),
    path(
        "<str:when_player>-<str:player_type>-leaders",
        views.leaderboards,
        name="leaderboards",
    ),
    path("search/", views.player_search, name="player-search"),
    path("player/<int:num>", views.player_detail, name="player-detail"),
]
