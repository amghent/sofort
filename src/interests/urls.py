from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>", views.index, name="interest_group_index"),
    path("<str:slug>/about", views.about, name="interest_group_about"),

    path("<str:slug>/under_construction", views.under_construction, name="interest_group_under_construction"),
]
