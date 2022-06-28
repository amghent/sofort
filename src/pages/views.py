from django.shortcuts import render


def detail(request, slug: str):
    # TODO: add a property to indicate if a page is visible to users who are not logged in
    from core.context import Context
    from pages.models import Page

    page = Page.objects.get(slug=slug)
    
    context = Context(request=request, current_page="pages_detail", slug=slug).get()
    context["page"] = page

    return render(request=request, template_name="pages/detail.jinja2", context=context)
