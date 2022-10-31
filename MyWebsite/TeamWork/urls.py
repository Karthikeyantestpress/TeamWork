from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        views.Greetings,
    ),
    path("login/", views.user_login, name="login"),
    path("login/Greetings", views.Welcome_Page, name="Welcome"),
    path("register/", views.register, name="Register"),
]
