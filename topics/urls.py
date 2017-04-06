from django.conf.urls import include, url
from .views import (
    home, 
    create_topic,
    downvote_topic,
    upvote_topic,
)

urlpatterns = [
    url(r'^create/$', create_topic, name='create-topic'),
    url(r'^list/$', home, name='home'),
    url(r'^(?P<topic_id>[^/]+)/upvote/$', upvote_topic, name='upvote-topic'),
    url(r'^(?P<topic_id>[^/]+)/downvote/$', downvote_topic, name='downvote-topic'),
]
