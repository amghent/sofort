from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>", views.interest_group_detail, name="interest_group_detail"),
]
