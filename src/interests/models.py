from django.db.models import ManyToManyField

###
# To avoid circular references, 
# put the factories for the SOFORT modules within the functions
# (except CoreModel which cannot be imported inline because of the inheritance)
###

from core.models import CoreModel


class InterestGroup(CoreModel):
    from core.models import UniqueCharField, MandatoryTextField, MandatoryCharField
    from members.models import Member

    name = UniqueCharField(max_length=30)
    slug = UniqueCharField(max_length=30)
    description = MandatoryCharField(max_length=150)
    about = MandatoryTextField()

    members = ManyToManyField(Member)

    def __str__(self):
        return f"{self.name} ({self.slug})"

    @property
    def member_count(self):
        return self.members.count()

    @property
    def question_count(self):
        from questions.models import Question

        return Question.objects.filter(interest_group=self).count()

    @property
    def question_response_count(self):
        from questions.models import QuestionResponse

        return QuestionResponse.objects.filter(question__interest_group=self).count()

    @property
    def question_comment_count(self):
        from questions.models import QuestionComment

        return QuestionComment.objects.filter(response__question__interest_group=self).count()
