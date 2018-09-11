from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views
from django.conf import settings # Import settings.py for usage

from projects.models import Project
from blog.models import Post

from django.core.mail import send_mail # Django core lib for sending emails!


# This is the index. I created a simple homepage view above
def index(request):
	projects = Project.objects.all() # Retrieve all projects
	template = loader.get_template('index.html')

	context = {
		'projects': projects,
	} # Ah context variables like Node to use in template. Cool
	
	return HttpResponse(template.render(context, request))


def contact(request):
	template = loader.get_template('contact.html')

	context = {} # Empty context for now

	return HttpResponse(template.render(context, request))