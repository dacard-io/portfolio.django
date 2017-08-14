from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views
from django.conf import settings # Import settings.py for usage

from projects.models import Project

# This is the tutorials index. I created a simple homepage view above
def index(request):
	projects = Project.objects.all() # Retrieve all projects
	template = loader.get_template('index.html')

	context = {
		#'latest_question_list': latest_question_list,
		'test_prop': 'Hello I am inside test prop',
		'projects': projects,
		'site_url': settings.SITE_URL
	} # Ah context variables like Node to use in template. Cool
	
	return HttpResponse(template.render(context, request))