from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserData(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    #    use= models.ForeignKey(User, on_delete=models.CASCADE)
    answeredQuestions = models.IntegerField(default=0)
    wrongQuestions = models.IntegerField(default=0)
    rightQuestions = models.IntegerField(default=0)


def __str__(self):
    return User.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userdata.save()