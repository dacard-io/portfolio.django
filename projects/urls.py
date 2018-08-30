from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views # import views.py from this app

urlpatterns = [
    url(r'^$', views.projects, name='projects'), # Leave this blank, since its already declared in root urlconf "url.com/project" or else it becomes "project/project"
    url(r'^(?P<project_id>[0-9]+)$', views.project, name='project'),
    url(r'^(?P<permalink>.*)$', views.project_permalink, name='project_permalink')
]