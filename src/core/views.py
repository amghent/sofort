from django.shortcuts import render

from core.context import *
from interests.models import InterestGroup


def index(request):
    meta = get_meta(current_page="home")
    #meta["current_page"] = "home"

    navigation_menu = get_navigation_menu()
    settings = get_settings()

    interest_groups = list(InterestGroup.objects.all())

    context = {
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "interest_groups": interest_groups
    }

    return render(request, "core/index.jinja2", context)
