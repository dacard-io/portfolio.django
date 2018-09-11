# Context processor for main app that makes data available to all templates without having to include to every page context!
# Include this file in settings.py in TEMPLATE_CONTEXT_PROCESSORS


from blog.models import Post
from app.settings import SITE_URL

def app_processor(request):
	recent_posts = Post.objects.filter(published=True).order_by('-pub_date')[:3] # Retrieve 3 objects and order by pub_date

	# Return data to template
	return {
		'recent_posts': recent_posts,
		'site_url': SITE_URL
	}

# Then simply call into template: {{recent_posts}}