from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login/post", views.login_user, name="login_user"),
    path("login/failure", views.login_failure, name="login_failure"),
    path("login/success", views.login_success, name="login_success"),
    path("logout", views.logout_user, name="logout_user")
]
