from django.utils import timezone
from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)


class Today_Todo(models.Model):
    title = models.CharField(max_length=200)
    Date_Created = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
