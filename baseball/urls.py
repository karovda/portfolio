from django.urls import path

from . import views

app_name = "baseball"
urlpatterns = [
    path("", views.baseball_home_view, name="baseball-home"),
    path("all-time-batting-leaders", views.alltime_batting, name="all-time-batting"),
    path("player/<int:num>", views.player_view, name="player-detail"),
]
