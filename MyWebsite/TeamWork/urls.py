from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path(
        "",
        views.Greetings,
    ),
    path("", include("django.contrib.auth.urls")),
    # path("login/", views.user_login, name="login"),
    path("login/Greetings", views.Welcome_Page, name="Welcome"),
    path("register/", views.register, name="Register"),
    path("Today_plan/", views.Todays_Plan, name="Todays_Plan"),
    path("Add_Todays_Plan/", views.Today_Plan_User_Input, name="Today_Plan_User_Input"),
]
urlpatterns += staticfiles_urlpatterns()
