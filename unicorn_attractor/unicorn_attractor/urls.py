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
from django.conf.urls import url
from django.contrib import admin
from accounts import views as accounts_views
from hello import views as hello_views
from bugs import views as forum_views
from feature_request import views as fr_views

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
    url(r'^feature_request_forum/$', fr_views.forum),
    url(r'^feature_requests/(?P<subject_id>\d+)/$', fr_views.feature_requests, name='feature_requests'),
    url(r'^new_feature_request/(?P<subject_id>\d+)/$',  fr_views.new_feature_request, name='new_feature_request'),
    url(r'^feature_request/(?P<feature_request_id>\d+)/$', fr_views.feature_request, name='feature_request'),
    url(r'^post/new/(?P<feature_requests_id>\d+)/$', fr_views.new_post, name='new_feature_request_post'),
    url(r'^post/edit/(?P<feature_requests_id>\d+)/(?P<post_id>\d+)/$',fr_views.edit_post, name='edit_feature_request_post'),
    url(r'^post/delete/(?P<feature_requests_id>\d+)/(?P<post_id>\d+)/$', fr_views.delete_post, name='delete_feature_request_post'),
    url(r'^feature_request/vote/(?P<feature_request_id>\d+)/(?P<subject_id>\d+)/$', fr_views.feature_request_vote, name='cast_feature_request_vote'),
]
