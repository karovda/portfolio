import json

from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render

from .forms import PlayerSearchForm
from .models import Batters, CareerStats, Pitchers, PlayerInfo


def baseball_home(request):
    return render(request, "baseball_base.html")


def player_detail(request, num):

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


def leaderboards(request, when_player, player_type):
    """
    This function takes two arguments each with only two acceptable inputs
    creating 4 possible outcomes. when_player can be either 'career' or 'current'
    and player_type can be 'batting' or 'pitching'.
    Any input not listed here will result in a 404 response.
    """
    career = False
    if when_player == "career":
        career = True
    elif when_player == "current":
        career = False
    else:
        raise Http404(
            "Try again with either career or current in /baseball/{whenplayer}-batting-leaders"
        )

    batting = False

    if player_type == "batting":
        batting = True
        if career:
            players = CareerStats.objects.select_related("player").order_by(
                "-bat_career"
            )[:500]
    elif player_type == "pitching":
        batting = False
        if career:
            players = CareerStats.objects.select_related("player").order_by(
                "-pit_career"
            )[:500]
    else:
        raise Http404(
            "Try again with either batting or pitching in /baseball/career-{player_type}-leaders"
        )

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
        },
    )


def player_search(request):
    form = PlayerSearchForm()
    query = ""
    results = []

    # POST here is initiated by the js fetch request.
    # It returns results to be listed in a dropdown area.
    if request.method == "POST":
        data = json.loads(request.body)
        search_string = data["ss"]

        if search_string is not None:
            dropdown_results = PlayerInfo.objects.filter(name__icontains=search_string)[
                :5
            ]
            # Run the custom serialize function on each result.
            return JsonResponse(
                [result.serialize() for result in dropdown_results], safe=False
            )

    if "q" in request.GET:
        form = PlayerSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["q"]
            results = PlayerInfo.objects.filter(name__icontains=query)

    return render(
        request,
        "search.html",
        {
            "form": form,
            "q": query,
            "results": results,
        },
    )
