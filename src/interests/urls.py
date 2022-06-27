from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>", views.interest_group_detail, name="interest_group_detail"),
    path("<str:slug>/about", views.interest_group_about, name="interest_group_about"),

    path("<str:slug>/under_construction", views.interest_group_under_construction, 
         name="interest_group_under_construction"),
]
