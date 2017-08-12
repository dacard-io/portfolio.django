from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views

from blog.models import Post
from projects.models import Project

# This is the tutorials index. I created a simple homepage view above
def index(request):
	#return HttpResponse("Hello World. Your at the polls index")
	#Get questions from the DB using the API. 
	#output = ', '.join([q.question_text for q in latest_question_list]) # Damn it I don't understand this line, need to read up on Python
	#return HttpResponse(output)
	recent_posts = Post.objects.order_by('-pub_date')[:5] # Retrieve all objects and order by pub_date
	projects = Project.objects.all() # Retrieve all projects
	template = loader.get_template('index.html')

	context = {
		#'latest_question_list': latest_question_list,
		'test_prop': 'Hello I am inside test prop',
		'recent_posts': recent_posts,
		'projects': projects
	} # Ah context variables like Node to use in template. Cool
	
	return HttpResponse(template.render(context, request))
	''' Shortcut way
	from django.shortcuts import render

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	'''