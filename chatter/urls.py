from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    # Examples:
    # url(r'^$', 'rsquarelabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('website.urls')),
    url(r'^api/beta0.6/', include('restful.urls')),
   
    # API Documentation
    url(r'^apidocs/beta0.6/', include('rest_framework_swagger.urls')),

]
