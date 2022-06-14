from django.shortcuts import render

from core.context import get_meta


def index(request):
    context = {
        "meta": get_meta()
    }

    return render(request, "core/index.html", context)
