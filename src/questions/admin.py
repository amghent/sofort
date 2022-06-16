from django.contrib import admin

from questions.models import Question, QuestionAnswer, QuestionDiscussion

admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(QuestionDiscussion)
