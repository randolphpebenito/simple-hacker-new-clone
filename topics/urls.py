from django.conf.urls import include, url
from .views import home, create_topic 

urlpatterns = [
    url(r'^all/$', home, name='home'),
    url(r'^create/$', create_topic, name='create-topic'),
]
