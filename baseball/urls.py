from django.urls import path

from . import views

app_name = "baseball"
urlpatterns = [
    path("", views.baseball_home_view),
    path("player/<int:num>", views.player_view),
]
