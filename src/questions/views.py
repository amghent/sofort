from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###
from questions.models import QuestionAnswer, QuestionDiscussion


def index(request, interest):
    # to avoid circular references, get_side_bar must be declared inline
    from core.context import get_meta, get_navigation_menu, get_settings
    from interests.context import get_side_bar
    from interests.models import InterestGroup
    from questions.models import Question

    interest_group = InterestGroup.objects.get(slug=interest)
    questions = Question.objects.filter(interest_group=interest_group).order_by("-created_at")

    load = {
        "sidebar": True,
        "datatables": True,
        "editor": False
    }
    meta = get_meta(current_page="questions_index", interest=interest)
    settings = get_settings()
    navigation_menu = get_navigation_menu()
    side_bar = get_side_bar(slug=interest)

    context = {
        "load": load,
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "side_bar": side_bar,
        "interest_group": interest_group,
        "questions": questions
    }

    return render(request, "questions/index.jinja2", context)


def detail(request, interest, uuid):
    # to avoid circular references, get_side_bar must be declared inline
    from core.context import get_meta, get_navigation_menu, get_settings
    from interests.context import get_side_bar
    from interests.models import InterestGroup
    from questions.models import Question

    interest_group = InterestGroup.objects.get(slug=interest)
    question = Question.objects.get(id=uuid)
    answers = QuestionAnswer.objects.filter(question=question.id)
    discussions = QuestionDiscussion.objects.filter(question_answer__question_id=question.id)

    load = {
        "sidebar": True,
        "datatables": False,
        "editor": True
    }
    meta = get_meta(current_page="questions_detail", interest=interest)
    settings = get_settings()
    navigation_menu = get_navigation_menu()
    side_bar = get_side_bar(slug=interest)

    context = {
        "load": load,
        "meta": meta,
        "settings": settings,
        "navigation_menu": navigation_menu,
        "side_bar": side_bar,
        "interest_group": interest_group,
        "question": question,
        "answers": answers,
        "discussions": discussions
    }

    return render(request, "questions/detail.jinja2", context)
