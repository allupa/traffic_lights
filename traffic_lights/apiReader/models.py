from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
#from django.contrib.gis.db import models as gismodels



    


# Create your models here.
#class Comment(models.Model):
#    comment = models.TextField(blank=False, max_length=500, default='')
 #   def __str__(self):
  #      return self.comment

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Device_detector(models.Model):
    device = models.CharField(max_length=100)
    detector = models.CharField(max_length=100)
    calcAmount = models.IntegerField(default=0)
    reliabValue = models.IntegerField(default=0)
    def __str__(self):
        return self.device