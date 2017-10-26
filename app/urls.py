"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views # import views.py from this app
from tinymce import urls # TinyMCE import
from filebrowser.sites import site # Filebrowser import

urlpatterns = [
    url(r'^$', views.index, name='index'), # Leaving the url as
    url(r'^manager/tinymce/', include('tinymce.urls')),
    url(r'^manager/', admin.site.urls),
    url(r'^manager/filebrowser/', include(site.urls)),
    url(r'^blog/', include('blog.urls')),
    # Include urls from blog app
    #url(r'^contact/', views.contact, name='contact') # Add contact form later
]
