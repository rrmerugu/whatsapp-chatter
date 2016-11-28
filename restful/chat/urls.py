__author__ = 'rrmerugu'
from django.conf.urls import include, url
from restful.chat import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^chat/list', views.ChatList.as_view()),
    url(r'^chat/buffer', views.ChatBufferList.as_view()),
    url(r'^chat/talk/(?P<kw>[a-zA-Z0-9 ]+)', views.TalktoMeList.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
