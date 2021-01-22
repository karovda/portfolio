from django.shortcuts import render
from django.core.paginator import Paginator

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


def alltime_batting(request):
    players = CareerStats.objects.select_related("player").order_by("-bat_career")[:100]
    paginator = Paginator(players, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "alltime_batting.html",
        {
            "page_obj": page_obj,
        },
    )
