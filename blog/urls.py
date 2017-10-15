from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views # import views.py from this app

urlpatterns = [
    url(r'^$', views.blog, name='blog'), # Leave this blank, since its already declared in root urlconf "url.com/blog" or else it becomes "blog/blog"
    url(r'^(?P<post_id>[0-9]+)$', views.post, name='post'),
    url(r'^(?P<permalink>.*)$', views.post_permalink, name='post_permalink')
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]