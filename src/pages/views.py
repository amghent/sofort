from django.shortcuts import render


def detail(request, slug):
    from core.context import get_default_context
    from pages.models import Page

    page = Page.objects.get(slug=slug)
    
    context = get_default_context(current_page="pages_detail", slug=slug)
    context["load"]["sidebar"] = False
    context["load"]["datatables"] = False
    context["load"]["editor"] = False
    context["page"] = page

    return render(request, "pages/detail.jinja2", context)
