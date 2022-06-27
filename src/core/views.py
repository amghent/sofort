from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def index(request):
    from core.context import Context
    from interests.models import InterestGroup

    interest_groups = list(InterestGroup.objects.all())

    context = Context(current_page="home").get()
    context["load"]["datatables"] = False
    context["load"]["sidebar"] = False
    context["load"]["editor"] = False
    context["interest_groups"] = interest_groups

    return render(request, "core/index.jinja2", context)
