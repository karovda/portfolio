from django.shortcuts import render

from .models import Batters, CareerStats, Pitchers, PlayerInfo


def baseball_home_view(request):
    return render(request, "baseball_base.html")


def player_view(request, num):

    return render(
        request,
        "player_detail.html",
        {
            "player": PlayerInfo.objects.get(pk=num),
            "batting": Batters.objects.filter(player=num).order_by("-year"),
            "pitching": Pitchers.objects.filter(player=num).order_by("-year"),
            "career": CareerStats.objects.get(player=num),
        },
    )
