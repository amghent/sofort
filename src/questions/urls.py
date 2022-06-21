from django.urls import path

from . import views

urlpatterns = [
    path("<str:interest>/", views.index, name="questions_index"),
    path("<str:interest>/new", views.new, name="questions_new"),
    path("<str:interest>/post", views.post, name="questions_post"),

    # because of the string in uuid, this must be defined after new and post
    path("<str:interest>/<str:uuid>", views.detail, name="questions_detail"),

]
