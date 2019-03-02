from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog),
    url(r'^create', views.create)
]