from django.conf.urls import url
from django.contrib import admin
from helloworld.views import helloWorld

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',helloWorld)
]
