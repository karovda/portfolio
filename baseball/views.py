import json

from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import PlayerSearchForm
from .models import Batters, CareerStats, Pitchers, PlayerInfo, StatDescriptions


def baseball_home(request):
    andruw = CareerStats.objects.get(player__name="Andruw Jones")
    edmonds = CareerStats.objects.get(player__name="Jim Edmonds")
    killebrew = CareerStats.objects.get(player__name="Harmon Killebrew")
    perez = CareerStats.objects.get(player__name="Tony Perez")
    return render(
        request,
        "baseball_index.html",
        {
            "firsts_and_centers": [killebrew, perez, edmonds, andruw],
            "table_headers": StatDescriptions.objects.get(pk=1),
        },
    )


def player_detail(request, num):

    return render(
        request,
        "player_detail.html",
        {
            "player": PlayerInfo.objects.get(pk=num),
            "batting": Batters.objects.filter(player=num).order_by("year"),
            "pitching": Pitchers.objects.filter(player=num).order_by("year"),
            "career": CareerStats.objects.get(player=num),
            "table_headers": StatDescriptions.objects.get(pk=1),
            "tool_tips": StatDescriptions.objects.get(pk=2),
        },
    )


def leaderboards(request, when_player, player_type):
    """
    This function takes two arguments each with only two acceptable inputs
    creating 4 possible outcomes. when_player can be either 'career' or 'current'
    and player_type can be 'batting' or 'pitching'.
    Any input not listed here will result in a 404 response.
    """
    career = ""
    if when_player == "career":
        career = True
    elif when_player == "current":
        career = False
    else:
        raise Http404(
            "Try again with either career or current in /baseball/{whenplayer}-batting-leaders"
        )

    batting = False

    players = CareerStats.objects.select_related("player")

    if player_type == "batting":
        batting = True
        if career:
            players = players.filter(bat_career__gte=20).order_by(
                "-bat_career", "player"
            )
        else:
            actives = PlayerInfo.objects.filter(last_year__in=[2019, 2020]).values_list(
                "id", flat=True
            )
            players = (
                players.filter(player__in=actives)
                .filter(career_pas__gte=500)
                .order_by("-bat_career", "player")
            )

    elif player_type == "pitching":
        batting = False
        if career:
            players = players.filter(pit_career__gte=20).order_by(
                "-pit_career", "player"
            )
        else:
            actives = PlayerInfo.objects.filter(last_year__in=[2019, 2020]).values_list(
                "id", flat=True
            )
            players = (
                players.filter(player__in=actives)
                .filter(career_ip__gte=150)
                .order_by("-pit_career", "player")
            )

    else:
        raise Http404(
            "Try again with either batting or pitching in /baseball/career-{player_type}-leaders"
        )

    table_headers = StatDescriptions.objects.get(pk=1)
    tool_tips = StatDescriptions.objects.get(pk=2)
    paginator = Paginator(players, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "leaderboards.html",
        {
            "page_obj": page_obj,
            "batting": batting,
            "career": career,
            "table_headers": table_headers,
            "tool_tips": tool_tips,
        },
    )


@csrf_exempt
def player_search(request):

    # POST here is initiated by the js fetch request.
    # It returns results to be listed in a dropdown area.
    if request.method == "POST":
        data = json.loads(request.body)
        search_string = data["ss"]

        if search_string is not None:
            dropdown_results = PlayerInfo.objects.filter(name__icontains=search_string)[
                :10
            ]
            # Run the custom serialize function on each result.
            return JsonResponse(
                [result.serialize() for result in dropdown_results], safe=False
            )

    form = PlayerSearchForm()
    query = ""
    results = []

    if "q" in request.GET:
        form = PlayerSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["q"]
            results = PlayerInfo.objects.filter(name__icontains=query).order_by(
                "-last_year", "name"
            )

    results_paginator = Paginator(results, 25)
    results_page_number = request.GET.get("page")
    results_page_obj = results_paginator.get_page(results_page_number)

    return render(
        request,
        "search.html",
        {
            "form": form,
            "q": query,
            "results": results,
            "page_obj": results_page_obj,
        },
    )


def the_stats(request):
    rose = CareerStats.objects.get(player=7496)
    votto = CareerStats.objects.get(player__name="Joey Votto")

    harper2015 = Batters.objects.filter(player__name="Bryce Harper").get(year=2015)
    bonds2003 = Batters.objects.filter(player__name="Barry Bonds").get(year=2003)
    return render(
        request,
        "the_stats.html",
        {
            "rose_votto": [rose, votto],
            "bonds_harper": [bonds2003, harper2015],
            "table_headers": StatDescriptions.objects.get(pk=1),
        },
    )
