from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>", views.detail, name="pages_detail"),
]
