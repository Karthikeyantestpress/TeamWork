from django.contrib import admin
from .models import Profile
from .models import Today_Todo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date_of_birth",
    ]


@admin.register(Today_Todo)
class Today_TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "Date_Created",
        "Created_by",
    ]

    class meta:
        ordering = "-Date_Created"
