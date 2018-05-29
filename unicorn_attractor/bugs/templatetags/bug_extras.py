import arrow
from django import template
from django.core.urlresolvers import reverse
 
register = template.Library()
 
@register.filter
def get_total_subject_posts(subject):
   total_posts = 0
   for bug in subject.bugs.all():
       total_posts += bug.posts.count()
   return total_posts

@register.filter
def started_time(created_at):
   return arrow.get(created_at).humanize()
 
 
@register.simple_tag
def last_posted_user_name(bug):
    last_post = bug.posts.all().order_by('created_at').last()
    return last_post.user.username