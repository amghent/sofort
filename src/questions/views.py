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
    from questions.models import Question, QuestionAnswer, QuestionReply

    question = Question.objects.get(id=question_uuid)

    context, _ = __common_context(request=request, interest_slug=interest_slug, current_page="questions_detail")
    context["question"] = question
    context["answers"] = QuestionAnswer.objects.filter(question=question.id).order_by("created_at")
    context["replies"] = QuestionReply.objects.filter(question_answer__question_id=question.id).order_by("created_at")

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
def answer(request, interest_slug: str, question_uuid: str):
    from questions.models import QuestionAnswer
    from members.context import Context as MemberContext

    question_answer = QuestionAnswer()

    question_answer.question_id = question_uuid
    question_answer.author = MemberContext.get_member_from_username(user=request.user)
    question_answer.text = request.POST["answer_text"]

    question_answer.save()

    return redirect(to="questions_detail", interest_slug=interest_slug, question_uuid=question_uuid)


@login_required
def reply(request, interest_slug: str, question_uuid: str, answer_uuid: str):
    from questions.models import QuestionReply
    from members.context import Context as MemberContext

    question_reply = QuestionReply()

    question_reply.question_answer_id = answer_uuid
    question_reply.author = MemberContext.get_member_from_username(user=request.user)
    question_reply.text = request.POST["reply_text"]

    question_reply.save()

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
