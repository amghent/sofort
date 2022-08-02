from django.urls import path

from . import views

urlpatterns = [
    path("<str:interest_slug>/", views.index, name="questions_index"),

    path("<str:interest_slug>/new", views.new, name="questions_new"),
    path("<str:interest_slug>/create", views.create, name="questions_create"),

    # because of the string in uuid, this must be defined after new and create
    path("<str:interest_slug>/<str:question_uuid>", views.read, name="questions_read"),

    path("<str:interest_slug>/<str:question_uuid>/respond", views.respond, name="questions_respond"),
    path("<str:interest_slug>/<str:question_uuid>/<str:response_uuid>/comment", views.comment, name="questions_comment"),

    path("<str:interest_slug>/<str:question_uuid>/<str:status>", views.read, name="questions_read"),
]
