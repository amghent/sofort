from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions 
###


def interest_group_detail(request, slug):
    from core.context import get_default_context
    from interests.models import InterestGroup
    from interests.context import get_sidebar
    
    interest_group = InterestGroup.objects.get(slug=slug)

    context = get_default_context(current_page="interest_group_detail", slug=slug, sidebar=True)
    context["load"]["datatables"] = False
    context["load"]["editor"] = False
    context["sidebar"] = get_sidebar(slug)
    context["interest_group"] = interest_group
    
    return render(request, "interests/interest_group_detail.jinja2", context)


def interest_group_about(request, slug):
    from core.context import get_default_context
    from interests.models import InterestGroup
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=slug)

    context = get_default_context(current_page="interest_group_about", slug=slug, sidebar=True)
    context["load"]["datatables"] = False
    context["load"]["editor"] = False
    context["sidebar"] = get_sidebar(slug)
    context["interest_group"] = interest_group

    return render(request, "interests/interest_group_about.jinja2", context)
