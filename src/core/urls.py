from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("login/post", views.check_login, name="check_login")
]
