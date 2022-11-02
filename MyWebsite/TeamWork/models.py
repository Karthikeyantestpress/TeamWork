from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)

    def __Unicode__(self):
        return self.user


class Today_Todo(models.Model):
    Created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )
    # Created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, default =1)
    title = models.CharField(max_length=200)
    Date_Created = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __Unicode__(self):
        return self.Created_by
