from typing import Any

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions
###


@login_required
def index(request, interest: str):
    from questions.models import Question

    context, interest_group = __common_context(request=request, interest=interest, current_page="questions_index")
    context["questions"] = Question.objects.filter(interest_group=interest_group).order_by("-created_at")

    return render(request=request, template_name="questions/index.jinja2", context=context)


@login_required
def detail(request, interest: str, uuid: str):
    from questions.models import Question, QuestionAnswer, QuestionDiscussion

    question = Question.objects.get(id=uuid)

    context, _ = __common_context(request=request, interest=interest, current_page="questions_detail")
    context["question"] = question
    context["answers"] = QuestionAnswer.objects.filter(question=question.id)
    context["discussions"] = QuestionDiscussion.objects.filter(question_answer__question_id=question.id)

    return render(request=request, template_name="questions/detail.jinja2", context=context)


@login_required
def new(request, interest: str):
    context, _ = __common_context(request=request, interest=interest, current_page="questions_new")

    return render(request=request, template_name="questions/new.jinja2", context=context)


@login_required
def post(request, interest: str):
    from questions.models import Question
    from members.context import Context as MemberContext

    context, interest_group = __common_context(request=request, interest=interest, current_page="questions_post")

    question = Question()

    question.title = request.POST["title"]
    question.text = request.POST["text"]
    question.author = MemberContext.get_member_from_username(user=request.user)
    question.interest_group = interest_group

    question.save()

    context["question"] = question

    return render(request=request, template_name="questions/detail.jinja2", context=context)


def __common_context(request, interest: str, current_page: str) -> (dict, Any):
    from interests.models import InterestGroup
    from core.context import Context
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=interest)

    context = Context(request=request, current_page=current_page, interest=interest).get()
    context["sidebar"] = get_sidebar(slug=interest)
    context["interest_group"] = interest_group

    return context, interest_group
