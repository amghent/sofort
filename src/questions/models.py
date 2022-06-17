from django.db import models

###
# To avoid circular references, 
# put the imports for the SOFORT modules within the functions 
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
    from core.fields import MandatoryCharField

    interest_group = models.ForeignKey(InterestGroup, on_delete=models.CASCADE)
    title = MandatoryCharField(max_length=250)
    
    class Meta:
        abstract = False
    
    
class QuestionAnswer(QuestionCommon):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        abstract = False


class QuestionDiscussion(QuestionCommon):
    question_answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)

    class Meta:
        abstract = False
