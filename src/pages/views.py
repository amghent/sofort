from django.shortcuts import render

from core.context import *
from pages.models import Page


def detail(request, slug):
    page = Page.objects.get(slug=slug)

    load = {
        "sidebar": False,
        "datatables": False,
        "editor": False
    }
    meta = get_meta(current_page="pages_detail", slug=slug)
    settings = get_settings()
    navigation_menu = get_navigation_menu()

    context = {
        "load": load,
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "page": page
    }

    return render(request, "pages/detail.jinja2", context)
