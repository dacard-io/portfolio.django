from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views
from django.conf import settings # Import settings.py for usage

from projects.models import Project

from .forms import ContactForm
from django.core.mail import send_mail # Django core lib for sending emails!


# This is the index. I created a simple homepage view above
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

def contact(request):
	if request.method == 'POST':
		# Create a form instance and populate it with data on request
		form = ContactForm(request.POST)
		# Check whether data was valid, and return success
		if form.is_valid():
			# Process data in form.cleaned_data
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['email']
			recipients = ['davidcardoso93@gmail.com']
			# Send email!
			send_mail(subject, message, sender, recipients)
			# Redirect
			return HttpResponseRedirect('/contact/')
	else:
		form = ContactForm()

	return render(request, 'contact.html', {'form': form})