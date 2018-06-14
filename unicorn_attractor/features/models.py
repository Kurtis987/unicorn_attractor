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

class Feature(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='features')
    subject = models.ForeignKey(Subject, related_name='features')
    created_at = models.DateTimeField(default=timezone.now)
    feature_votes_count = models.IntegerField(default=0)


class Post(models.Model):
    feature = models.ForeignKey(Feature, related_name='feature_posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feature_posts')
    created_at = models.DateTimeField(default=timezone.now)

class Vote(models.Model):
    feature = models.ForeignKey(Feature, related_name='feature_votes') 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feature_votes')