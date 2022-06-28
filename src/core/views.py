from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def index(request):
    from core.context import Context
    from interests.models import InterestGroup

    context = Context(request=request, current_page="home").get()

    member = context["member"]

    if member is None:
        interest_groups = []
    else:
        interest_groups = list(InterestGroup.objects.filter(members__in=[member]))

    context["interest_groups"] = interest_groups

    return render(request=request, template_name="core/index.jinja2", context=context)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request=request, username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request=request, user=user)

            return redirect(to="login_success")

    return redirect(to="login_failure")


def logout_user(request):
    logout(request=request)

    return redirect(to="index")


def login_failure(request):
    # TODO: this must be removed and become one index page, but don't know how to do it yet

    from core.context import Context
    from interests.models import InterestGroup

    context = Context(request=request, current_page="login_failure").get()

    member = context["member"]

    if member is None:
        interest_groups = []
    else:
        interest_groups = list(InterestGroup.objects.filter(members__in=[member]))

    context["interest_groups"] = interest_groups
    context["message"] = {
        "status": "ERROR",
        "text": "Login failed !"
    }

    return render(request=request, template_name="core/index.jinja2", context=context)


def login_success(request):
    # TODO: this must be removed and become one index page, but don't know how to do it yet

    from core.context import Context
    from interests.models import InterestGroup

    context = Context(request=request, current_page="login_success").get()

    member = context["member"]

    if member is None:
        interest_groups = []
    else:
        interest_groups = list(InterestGroup.objects.filter(members__in=[member]))

    context["interest_groups"] = interest_groups

    context["message"] = {
        "status": "SUCCESS",
        "text": "Login successful !"
    }

    return render(request=request, template_name="core/index.jinja2", context=context)
