from django.conf.urls import url
from website import views

urlpatterns = [
    # Examples
    url(r'^$', views.landing, name='home'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^all-chat-data', views.chatdata, name='chatdata'),

]
