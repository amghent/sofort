from django.shortcuts import render

from core.context import get_meta
from core.models import Setting
from interests.models import InterestGroup


def index(request):
    meta = get_meta()
    meta["current_page"] = "index.html"

    settings_data = Setting.objects.all()
    settings = {}

    for setting in settings_data:
        settings[setting.name] = setting.text

    interest_groups = list(InterestGroup.objects.all())

    context = {
        "meta": meta,
        "settings": settings,
        "interest_groups": interest_groups
    }

    return render(request, "core/index.html", context)
