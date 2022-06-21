from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


def index(request, interest):
    from questions.models import Question

    context, interest_group = __common_context(interest=interest, current_page="questions_index")
    context["load"]["editor"] = False  # Override
    context["questions"] = Question.objects.filter(interest_group=interest_group).order_by("-created_at")

    return render(request, "questions/index.jinja2", context)


def detail(request, interest, uuid):
    from questions.models import Question, QuestionAnswer, QuestionDiscussion

    context, interest_group = __common_context(interest=interest, current_page="questions_detail")

    question = Question.objects.get(id=uuid)

    context["datatables"] = False
    context["question"] = question
    context["answers"] = QuestionAnswer.objects.filter(question=question.id)
    context["discussions"] = QuestionDiscussion.objects.filter(question_answer__question_id=question.id)

    return render(request, "questions/detail.jinja2", context)


def new(request, interest):
    context, interest_group = __common_context(interest=interest, current_page="questions_new")

    context["datatables"] = False

    return render(request, "questions/new.jinja2", context)


def post(request, interest):
    from questions.models import Question
    from members.models import Member

    context, interest_group = __common_context(interest=interest, current_page="questions_post")

    question = Question()

    question.title = request.POST["title"]
    question.text = request.POST["text"]
    question.author = Member.objects.get(member_name="sidviny")
    question.interest_group = interest_group

    question.save()


    context["question"] = question

    return render(request=request, template_name="questions/detail.jinja2", context=context)


def __common_context(interest, current_page):
    from interests.models import InterestGroup
    from core.context import get_meta, get_navigation_menu, get_settings
    from interests.context import get_side_bar

    interest_group = InterestGroup.objects.get(slug=interest)

    load = {
        "sidebar": True,
        "datatables": True,
        "editor": True
    }

    meta = get_meta(current_page=current_page, interest=interest)
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
    }

    return context, interest_group
