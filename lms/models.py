from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser



# Create your models here.
class LmsModel(models.Model):
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    time = models.DateTimeField(null=True, blank=True, default=timezone.now)
    memo = models.TextField(null=True, blank=True, default='')
    # user_id = models.ForeignKey('User', on_delete=models.CASCADE)

class GoalModel(models.Model):
    goal = models.IntegerField(null=True)