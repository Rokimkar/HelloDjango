from django.conf.urls import url
from django.contrib import admin
from helloworld.views import helloWorld,current_datetime,giveAllPublishers, giveAllBooks


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',helloWorld),
    url(r'^time/$',current_datetime),
    url(r'^all_publishers/$',giveAllPublishers),
    url(r'^all_books/$',giveAllBooks)
]


