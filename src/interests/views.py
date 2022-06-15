from wsgiref.util import request_uri
from django.shortcuts import render

from core.context import *
from interests.models import InterestGroup

def get_side_bar(slug):
    sb = [
        {"href": f"/i/{slug}", "title": "Dashboard"},
        {"href": f"/pages/under_construction", "title": "Bookmarks"},
        {"href": f"/pages/under_construction", "title": "Questions"},
        {"href": f"/pages/under_construction", "title": "Issues"},
        {"href": f"/pages/under_construction", "title": "Forums"},
        {"href": f"/pages/under_construction", "title": "Tutorials"},
        {"href": f"/pages/under_construction", "title": "Newsletters"},
        {"href": f"/pages/under_construction", "title": "Tags"},
        {"href": f"/pages/under_construction", "title": "Links"},
        {"href": f"/i/{slug}/about", "title": "About"},
    ]

    return sb
    

def interest_group_detail(request, slug):
    interest_group = InterestGroup.objects.get(slug=slug)

    meta = get_meta(current_page="interest_group_detail", slug=slug, side_bar=True)
    navigation_menu = get_navigation_menu()
    settings = get_settings()
    sidebar = get_side_bar(slug)
    
    context = {
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "sidebar": sidebar,
        "interest_group": interest_group
    }

    return render(request, "interests/interest_group_detail.jinja2", context)

def interest_group_about(request, slug):
    interest_group = InterestGroup.objects.get(slug=slug)
    
    meta = get_meta(current_page="interest_group_about", slug=slug, side_bar=True)
    navigation_menu = get_navigation_menu()
    settings = get_settings()
    sidebar = get_side_bar(slug)

    context = {
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "sidebar": sidebar,
        "interest_group": interest_group
    }

    return render(request, "interests/interest_group_about.jinja2", context)
