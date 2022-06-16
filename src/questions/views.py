from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###

def index(request, interest):
    # to avoid circular references, get_side_bar must be declared inline
    from core.context import get_meta, get_navigation_menu, get_settings
    from interests.context import get_side_bar
    from interests.models import InterestGroup
    from questions.models import Question

    meta = get_meta(current_page="questions_index", interest=interest)
    navigation_menu = get_navigation_menu()
    settings = get_settings()
    side_bar = get_side_bar(slug=interest)

    interest_group = InterestGroup.objects.get(slug=interest)
    questions = Question.objects.filter(interest_group=interest_group)

    context = {
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "side_bar": side_bar,
        "interest_group": interest_group,
        "questions": questions
    }

    return render(request, "questions/index.jinja2", context)
