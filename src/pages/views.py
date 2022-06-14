from django.shortcuts import render

from core.context import *
from pages.models import Page


def detail(request, slug):
    meta = get_meta()
    meta["current_page"] = "pages_detail"
    meta["slug"] = slug

    navigation_menu = get_navigation_menu()
    settings = get_settings()

    page = Page.objects.get(slug=slug)

    context = {
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "page": page
    }

    return render(request, "pages/detail.html", context)
