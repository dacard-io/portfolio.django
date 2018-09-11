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
	queryset = Post.objects.order_by('-pub_date') # Retrieve all objects and order by pub_date
	
	# Get URL param "tag" to do basic filtering
	tag_query = request.GET.get('tag', '') # Second param is the default value if nothing is found

	# If tag query found, filter posts by tag
	if tag_query:
		queryset = queryset.filter(tag__icontains=tag_query)

	template = loader.get_template('blog.html')

	context = {
		'casestudies_available': any(post.tag == "case-studies" for post in queryset),
		'tutorials_available': any(post.tag == "tutorials" for post in queryset),
		'projectlogs_available': any(post.tag == "project-logs" for post in queryset),
		'blog_posts': queryset,
		'site_url': settings.SITE_URL
	}

	return HttpResponse(template.render(context, request))

# Post view (by ID)
def post(request, post_id):
	queryset = get_object_or_404(Post, pk=post_id)
	template = loader.get_template('post.html')

	context = {
		'post': queryset
	}

	return HttpResponse(template.render(context, request))

def post_permalink(request, permalink):
	#queryset = Post.objects.filter(permalink=permalink)
	queryset = get_object_or_404(Post, permalink=permalink)
	template = loader.get_template('post.html')

	context = {
		'post': queryset
	}

	return HttpResponse(template.render(context, request))