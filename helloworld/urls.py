from django.conf.urls import url
from django.contrib import admin
from helloworld.views import helloWorld,current_datetime,giveAllPublishers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',helloWorld),
    url(r'^time/$',current_datetime),
    url(r'^all_publishers/$',giveAllPublishers)
]


