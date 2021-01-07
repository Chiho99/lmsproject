from django.db import models
from django.utils import timezone

# Create your models here.
class LmsModel(models.Model):
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    time = models.DateTimeField(null=True, blank=True, default=timezone.now)
    memo = models.TextField(null=True, blank=True, default='')
   
class GoalModel(models.Model):
    goal = models.IntegerField(null=True)
