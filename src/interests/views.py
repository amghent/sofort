from django.contrib.auth.decorators import login_required
from django.shortcuts import render

###
# To avoid circular references, 
# put the factories for the SOFORT modules within the functions
###


@login_required
def index(request, slug: str):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar
    
    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_detail", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug=slug)
    context["interest_group"] = interest_group
    
    return render(request=request, template_name="interests/index.jinja2", context=context)


@login_required
def about(request, slug: str):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_about", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug=slug)
    context["interest_group"] = interest_group

    return render(request=request, template_name="interests/about.jinja2", context=context)


@login_required
def under_construction(request, slug: str):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_under_construction", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug=slug)
    context["interest_group"] = interest_group

    return render(request=request, template_name="interests/under_construction.jinja2", context=context)
