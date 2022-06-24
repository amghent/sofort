from django.shortcuts import render


def detail(request, slug):
    from core.context import Context
    from pages.models import Page

    page = Page.objects.get(slug=slug)
    
    context = Context(current_page="pages_detail", slug=slug).get()
    context["load"]["sidebar"] = False
    context["load"]["datatables"] = False
    context["load"]["editor"] = False
    context["page"] = page

    return render(request, "pages/detail.jinja2", context)
