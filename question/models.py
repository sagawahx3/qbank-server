from django.db import models


class Question(models.Model):
    institute = models.CharField(
        max_length=12,
        null=True
    )
    question_number = models.CharField(
        max_length=12,
        null=True
    )
    version = models.CharField(
        max_length=12,
        null=True
    )
    body = models.TextField(
        null=True
    )
    ans1 = models.TextField(
        null=True
    )
    ans2 = models.TextField(
        null=True
    )
    ans3 = models.TextField(
        null=True
    )
    ans4 = models.TextField(
        null=True
    )
    ans5 = models.TextField(
        null=True
    )
    correct = models.PositiveIntegerField(
        max_length=1,
        null=True
    )

    def __str__(self):
        return self.question_number
