from django.urls import path

from . import views

urlpatterns = [
    path("<str:interest>/", views.index, name="questions_index"),
]
