from django.db import models
from django.utils import timezone # To calculate by timezone
from django.urls import reverse
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60,help_text="60 character limit")
	description = models.CharField(max_length=150,help_text="150 character limit")

	tag_choices = (
		('uncategorized', 'Uncategorized'),
		('case-studies', 'Web Apps'),
		('tutorials', 'Tutorials'),
		('project-logs', 'Project Logs')
	) # Remember, the first parameter is set in the DB. The second is the one to appear in labels
	tag = models.CharField(max_length=60, choices=tag_choices, default="uncategorized", help_text="Tag your post for categorization.")

	content = tinymce_models.HTMLField(blank=True, help_text='To use Prism.js for code: <pre><code class="language-css">p { color: red }</code></pre>')
	pub_date = models.DateTimeField('date published')
	published = models.BooleanField('enabled')

	# Permalink field (important)
	permalink = models.SlugField(max_length=40, unique=True, blank=True)

	# Add a method for showing whether a question was published recently
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	# To prevent outputting <Question: Question Object> which is not helpful for examination, we can fix that by
	# adding this __str__ method to the class to actually see whats in the object
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# Make title URL safe
		'''
		url = self.title
		url = url.lower()
		url = url.replace(" ", "-")
		url = url.replace("'", "")
		url = url.replace(".", "")
		'''

		#return '/%s/' % url
		#return '/%s/' % self.permalink
		return reverse('post_permalink', kwargs={"permalink": self.permalink})