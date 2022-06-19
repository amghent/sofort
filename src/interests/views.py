from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions 
###


def interest_group_detail(request, slug):
    from core.context import get_meta, get_settings, get_navigation_menu
    from interests.models import InterestGroup
    from interests.context import get_side_bar
    
    interest_group = InterestGroup.objects.get(slug=slug)

    load = {
        "sidebar": True,
        "datatables": False,
        "editor": False
    }
    meta = get_meta(current_page="interest_group_detail", slug=slug, side_bar=True)
    settings = get_settings()
    navigation_menu = get_navigation_menu()
    side_bar = get_side_bar(slug)
    
    context = {
        "load": load,
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "side_bar": side_bar,
        "interest_group": interest_group
    }

    return render(request, "interests/interest_group_detail.jinja2", context)


def interest_group_about(request, slug):
    from core.context import get_meta, get_settings, get_navigation_menu
    from interests.models import InterestGroup
    from interests.context import get_side_bar

    interest_group = InterestGroup.objects.get(slug=slug)

    load = {
        "sidebar": True,
        "datatables": False,
        "editor": False
    }
    meta = get_meta(current_page="interest_group_about", slug=slug, side_bar=True)
    settings = get_settings()
    navigation_menu = get_navigation_menu()
    side_bar = get_side_bar(slug)

    context = {
        "load": load,
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "side_bar": side_bar,
        "interest_group": interest_group
    }

    return render(request, "interests/interest_group_about.jinja2", context)
