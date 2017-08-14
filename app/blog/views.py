from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render #Import for rendering templates
from django.http import Http404 #Import 404s
from django.urls import reverse # For going back a page with forms
from django.views import generic # For generic class-based views
from django.conf import settings # Import settings.py for usage

from .models import Post

# Create your views here.
def blog(request):
	recent_posts = Post.objects.order_by('-pub_date')[:5] # Retrieve all objects and order by pub_date
	template = loader.get_template('blog.html')

	print("Blog page initiated")

	context = {
		'recent_posts': recent_posts,
		'site_url': settings.SITE_URL
	}

	return HttpResponse(template.render(context, request))