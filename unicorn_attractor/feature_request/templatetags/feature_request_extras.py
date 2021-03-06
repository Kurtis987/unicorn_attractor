import arrow
from django import template
from django.core.urlresolvers import reverse
 
register = template.Library()
 
@register.filter
def get_total_subject_posts(subject):
   total_posts = 0
   for feature_request in subject.feature_requests.all():
       total_posts += feature_request.feature_request_posts.count()
   return total_posts

@register.filter
def started_time(created_at):
   return arrow.get(created_at).humanize()
 
 
@register.simple_tag
def last_posted_user_name(feature_request):
    last_post = feature_request.feature_request_posts.all().order_by('created_at').last()
    return last_post.user.username


@register.simple_tag
def user_vote_button(feature_request, subject, user):
    vote = feature_request.feature_request_votes.filter(user_id=user.id).first()
 
    if not vote:
        if user.is_authenticated():
            link = """
            <div class="col-md-3 btn-vote"> 
            <a href="%s" class="btn btn-default btn-sm">
              Add my vote!
            </a>
            </div>""" % reverse('cast_vote', kwargs={'feature_request_id' : feature_request.id, 'subject_id':feature_request.subject_id})
 
            return link
 
    return ""

@register.filter
def vote_count(subject):
   count = subject.feature_request_votes.count()
   if count == 0:
       return 0
   total_votes = subject.feature_request_votes.count()
   return total_votes