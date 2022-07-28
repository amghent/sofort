from typing import Any

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


###
# To avoid circular references, 
# put the factories for the SOFORT modules within the functions
###


@login_required
def index(request, interest_slug: str):
    from questions.models import Question

    context, interest_group = __common_context(request=request, interest_slug=interest_slug,
                                               current_page="questions_index")
    context["questions"] = Question.objects.filter(interest_group=interest_group)

    return render(request=request, template_name="questions/index.jinja2", context=context)


@login_required
def detail(request, interest_slug: str, question_uuid: str):
    from questions.models import Question, QuestionResponse, QuestionComment

    question = Question.objects.get(id=question_uuid)

    context, _ = __common_context(request=request, interest_slug=interest_slug, current_page="questions_detail")
    context["question"] = question
    context["responses"] = QuestionResponse.objects.filter(question=question.id).order_by("created_at")
    context["comments"] = QuestionComment.objects.filter(response__question_id=question.id).order_by("created_at")

    return render(request=request, template_name="questions/detail.jinja2", context=context)


@login_required
def new(request, interest_slug: str):
    context, _ = __common_context(request=request, interest_slug=interest_slug, current_page="questions_new")

    return render(request=request, template_name="questions/new.jinja2", context=context)


@login_required
def save(request, interest_slug: str):
    from interests.models import InterestGroup
    from questions.models import Question
    from members.context import Context as MemberContext

    question = Question()

    question.title = request.POST["question_title"]
    question.text = request.POST["question_text"]
    question.author = MemberContext.get_member_from_username(user=request.user)
    question.interest_group = InterestGroup.objects.get(slug=interest_slug)

    question.save()

    return redirect(to="questions_detail", interest_slug=interest_slug, question_uuid=question.id)


@login_required
def respond(request, interest_slug: str, question_uuid: str):
    from questions.models import QuestionResponse
    from members.context import Context as MemberContext

    question_response = QuestionResponse()

    question_response.question_id = question_uuid
    question_response.author = MemberContext.get_member_from_username(user=request.user)
    question_response.text = request.POST["response_text"]

    question_response.save()

    return redirect(to="questions_detail", interest_slug=interest_slug, question_uuid=question_uuid)


@login_required
def comment(request, interest_slug: str, question_uuid: str, response_uuid: str):
    from questions.models import QuestionComment
    from members.context import Context as MemberContext

    question_comment = QuestionComment()

    question_comment.response_id = response_uuid
    question_comment.author = MemberContext.get_member_from_username(user=request.user)
    question_comment.text = request.POST["comment_text"]

    question_comment.save()

    return redirect(to="questions_detail", interest_slug=interest_slug, question_uuid=question_uuid)


def __common_context(request, interest_slug: str, current_page: str) -> (dict, Any):
    from interests.models import InterestGroup
    from core.context import Context
    from interests.context import get_sidebar

    interest_group = InterestGroup.objects.get(slug=interest_slug)

    context = Context(request=request, current_page=current_page, interest=interest_slug).get()
    context["sidebar"] = get_sidebar(slug=interest_slug)
    context["interest_group"] = interest_group

    return context, interest_group
