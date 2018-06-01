from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings
from django.utils import timezone
 
class Subject(models.Model):
 
    name = models.CharField(max_length=255)
    description = HTMLField()
 
    def __unicode__(self):
        return self.name

class FeatureRequest(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feature_requests')
    subject = models.ForeignKey(Subject, related_name='feature_requests')
    created_at = models.DateTimeField(default=timezone.now)
    feature_votes = models.IntegerField(default=0)
    status_choices = ['todo', 'doing', 'done']
    status = models.IntegerField(default=0)

class Post(models.Model):
    featureRequest = models.ForeignKey(FeatureRequest, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)

class Vote(models.Model):
    featureRequest = models.ForeignKey(FeatureRequest, related_name='votes')
    #poll = models.ForeignKey(Poll, related_name="votes")
    #subject = models.ForeignKey(Subject, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')

# Create your models here.
