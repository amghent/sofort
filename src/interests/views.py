from django.contrib.auth.decorators import login_required
from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions 
###


@login_required
def interest_group_detail(request, slug):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar
    
    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_detail", slug=slug, sidebar=True).get()
    context["load"]["datatables"] = False
    context["load"]["editor"] = False
    context["sidebar"] = get_sidebar(slug)
    context["interest_group"] = interest_group
    
    return render(request, "interests/interest_group_detail.jinja2", context)


@login_required
def interest_group_about(request, slug):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_about", slug=slug, sidebar=True).get()
    context["load"]["datatables"] = False
    context["load"]["editor"] = False
    context["sidebar"] = get_sidebar(slug)
    context["interest_group"] = interest_group

    return render(request, "interests/interest_group_about.jinja2", context)


@login_required
def interest_group_under_construction(request, slug):
    from core.context import Context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = Context(request=request, current_page="interest_group_under_construction", slug=slug, sidebar=True).get()
    context["sidebar"] = get_sidebar(slug)
    context["interest_group"] = interest_group

    return render(request, "interests/interest_group_under_construction.jinja2", context)
