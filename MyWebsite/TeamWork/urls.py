from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.Greetings,
    ),
    path("login/", views.user_login, name="login"),
    path("login/Greetings", views.Welcome_Page, name="Welcome"),
    path("register/", views.register, name="Register"),
    path("Today_plan/", views.Todays_Plan, name="Todays_Plan"),
    path("Add_Todays_Plan/", views.Today_Plan_User_Input, name="Today_Plan_User_Input"),
]
