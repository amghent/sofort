from django.urls import path

from . import views

urlpatterns = [
    path("<str:interest>/", views.index, name="questions_index"),
    path("<str:interest>/<str:uuid>", views.detail, name="questions_detail"),
]
