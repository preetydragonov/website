from django.conf.urls import url, include, patterns
from helloWorld.views import hello

urlpatterns = patterns('',
     url(r'^hello/$', hello)
                      )
