from django.shortcuts import render

from core.context import *
from interests.models import InterestGroup


def interest_group_detail(request, slug):
    meta = get_meta()
    meta["current_page"] = "interest_group_detail"
    meta["slug"] = slug

    navigation_menu = get_navigation_menu()
    settings = get_settings()

    interest_group = InterestGroup.objects.get(slug=slug)

    context = {
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "interest_group": interest_group
    }

    return render(request, "interests/interest_group_detail.html", context)
