from django.contrib import admin

from questions.models import Question, QuestionResponse, QuestionComment

admin.site.register(Question)
admin.site.register(QuestionResponse)
admin.site.register(QuestionComment)
