from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views
from django.conf import settings # Import settings.py for usage

from .models import Project
from .models import ProjectImage

# Create your views here.
def projects(request):
	queryset = Project.objects.order_by('order') # Retrieve all objects and order by field "order"

	# Get URL param "tag" to do basic filtering
	tag_query = request.GET.get('tag', '') # Second param is the default value if nothing is found

	# If tag query found, filter projects by tag
	if tag_query:
		queryset = queryset.filter(tag__icontains=tag_query)

	template = loader.get_template('projects.html')

	context = {
		'projects': queryset,
		'site_url': settings.SITE_URL
	}

	return HttpResponse(template.render(context, request))

# Project view (by ID)
def project(request, project_id):
	queryset = get_object_or_404(Project, pk=project_id)
	queryset_projectImages = ProjectImage.objects.filter(project_id=queryset.pk)
	template = loader.get_template('project.html')

	print(queryset_projectImages)

	context = {
		'project': queryset,
		'project_images': queryset_projectImages,
	}

	return HttpResponse(template.render(context, request))

def project_permalink(request, permalink):
	#queryset = Project.objects.filter(permalink=permalink)
	queryset = get_object_or_404(Project, permalink=permalink)
	queryset_projectImages = ProjectImage.objects.filter(project_id=queryset.pk)
	template = loader.get_template('project.html')

	print(queryset_projectImages)

	context = {
		'project': queryset,
		'project_images': queryset_projectImages
	}

	return HttpResponse(template.render(context, request))