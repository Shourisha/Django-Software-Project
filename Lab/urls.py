from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^people/$', views.worker),
    url(r'^project/$', views.projects),
    url(r'^people/(?P<name>[0-9a-zA-Z_]+)', views.displaysingleworker),
    url(r'^project/(?P<name>[0-9a-zA-Z_]+)', views.displaysingleproject)
]