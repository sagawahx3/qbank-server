from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    totalAnswers = models.PositiveIntegerField(default=0)
    rightAnswers = models.PositiveIntegerField(default=0)
    wrongAnswers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.id