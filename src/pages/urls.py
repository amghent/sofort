from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>", views.detail, name="page_detail"),
]
