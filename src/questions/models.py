from django.db import models

###
# To avoid circular references, 
# put the factories for the SOFORT modules within the functions
# (except CoreModel which cannot be imported inline because of the inheritance)
###

from core.fields import CoreModel


class QuestionCommon(CoreModel):
    from members.models import Member
    from core.fields import MandatoryTextField, DefaultFieldNow, OptionalTimestampField

    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    text = MandatoryTextField()
    
    created_at = DefaultFieldNow()
    last_updated_at = OptionalTimestampField()
    
    class Meta:
        abstract = True


class Question(QuestionCommon):
    from interests.models import InterestGroup
    from core.fields import MandatoryCharField, OptionalBigIntegerField

    interest_group = models.ForeignKey(InterestGroup, on_delete=models.CASCADE)
    title = MandatoryCharField(max_length=250)
    view_count = OptionalBigIntegerField()

    # TODO: verify if the properties below do not cause too many queries. If so, de-normalise and make it a property
    @property
    def response_count(self):
        return QuestionResponse.objects.filter(question_id=self.id).count()

    @property
    def comment_count(self):
        return QuestionComment.objects.filter(response__question_id=self.id).count()

    class Meta:
        abstract = False
    
    
class QuestionResponse(QuestionCommon):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        abstract = False


class QuestionComment(QuestionCommon):
    response = models.ForeignKey(QuestionResponse, on_delete=models.CASCADE)

    class Meta:
        abstract = False
