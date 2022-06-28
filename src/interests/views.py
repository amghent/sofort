from django.contrib.auth.decorators import login_required
from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions 
###


@login_required
def interest_group_detail(request, slug: str):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar
    
    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_detail", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug=slug)
    context["interest_group"] = interest_group
    
    return render(request=request, template_name="interests/interest_group_detail.jinja2", context=context)


@login_required
def interest_group_about(request, slug: str):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_about", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug=slug)
    context["interest_group"] = interest_group

    return render(request=request, template_name="interests/interest_group_about.jinja2", context=context)


@login_required
def interest_group_under_construction(request, slug: str):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_under_construction", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug=slug)
    context["interest_group"] = interest_group

    return render(request=request, template_name="interests/interest_group_under_construction.jinja2", context=context)
