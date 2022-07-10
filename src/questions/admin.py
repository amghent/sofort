from django.contrib import admin

from questions.models import Question, QuestionAnswer, QuestionReply

admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(QuestionReply)
