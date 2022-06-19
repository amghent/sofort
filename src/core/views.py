from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def index(request):
    from core.context import get_meta, get_navigation_menu, get_settings
    from interests.models import InterestGroup

    interest_groups = list(InterestGroup.objects.all())

    load = {
        "sidebar": False,
        "datatables": False,
        "editor": False
    }
    meta = get_meta(current_page="home")
    settings = get_settings()
    navigation_menu = get_navigation_menu()

    context = {
        "load": load,
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "interest_groups": interest_groups
    }

    return render(request, "core/index.jinja2", context)
