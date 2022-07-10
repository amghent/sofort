from django.urls import path

from . import views

urlpatterns = [
    path("<str:interest_slug>/", views.index, name="questions_index"),
    path("<str:interest_slug>/new", views.new, name="questions_new"),
    path("<str:interest_slug>/save", views.save, name="questions_save"),

    # because of the string in uuid, this must be defined after new and post
    path("<str:interest_slug>/<str:question_uuid>", views.detail, name="questions_detail"),
    path("<str:interest_slug>/<str:question_uuid>/answer", views.answer, name="questions_answer"),
    path("<str:interest_slug>/<str:question_uuid>/<str:answer_uuid>reply", views.reply, name="questions_reply"),
]
