"""unicorn_attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from hello import views as hello_views
from bugs import views as forum_views
from features import views as feature_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^forum/$', forum_views.forum),
    url(r'^bugs/(?P<subject_id>\d+)/$', forum_views.bugs, name='bugs'),
    url(r'^new_bug/(?P<subject_id>\d+)/$',  forum_views.new_bug, name='new_bug'),
    url(r'^bug/(?P<bug_id>\d+)/$', forum_views.bug, name='bug'),
    url(r'^post/new/(?P<bug_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<bug_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<bug_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^bug/vote/(?P<bug_id>\d+)/(?P<subject_id>\d+)/$', forum_views.bug_vote, name='cast_vote'),
    url(r'^feature_forum/$', feature_views.feature_forum, name='feature_forum'),
    url(r'^features/(?P<subject_id>\d+)/$', feature_views.features, name='features'),
    url(r'^new_feature/(?P<subject_id>\d+)/$',  feature_views.new_feature, name='new_feature'),
    url(r'^feature/(?P<feature_id>\d+)/$', feature_views.feature, name='feature'),
    url(r'^post/new/(?P<feature_id>\d+)/$', feature_views.new_post, name='new_feature_post'),
    url(r'^post/edit/(?P<feature_id>\d+)/(?P<post_id>\d+)/$',feature_views.edit_post, name='edit_feature_post'),
    url(r'^post/delete/(?P<feature_id>\d+)/(?P<post_id>\d+)/$', feature_views.delete_post, name='delete_feature_post'),
    url(r'^feature/vote/(?P<feature_id>\d+)/(?P<subject_id>\d+)/$', feature_views.feature_vote, name='cast_feature_vote'),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]
