from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from tinymce import models as tinymce_models
from django.urls import reverse
from django.conf.urls.static import static # To get static directories to show thumbnail
from app.settings import SITE_URL

# Create your models here.
class Project(models.Model):

	title = models.CharField(max_length=60,help_text="60 character limit")
	order = models.PositiveIntegerField(default=0, blank=False, null=False) #adminSortable field

	tag_choices = (
		('uncategorized', 'Uncategorized'),
		('web-app', 'Web Apps'),
		('android-app', 'Android Apps'),
		('website', 'Websites'),
		('ecommerce', 'e-Commerce'),
		('plugins-extensions', 'Plugins & Extensions'),
	) # Remember, the first parameter is set in the DB. The second is the one to appear in labels
	tag = models.CharField(max_length=60, choices=tag_choices, default="uncategorized", help_text="Tag your project for categorization.")
	
	description = models.TextField(max_length=255, help_text="Describe your project. (255 character limit)")
	stack = models.CharField(max_length=255, blank=True, help_text="Describe your project's used tech stack. (255 character limit)")
	link = models.CharField(max_length=255, blank=True, help_text="Enter the link to your project. (255 character limit)")
	source = models.CharField(max_length=255, blank=True, help_text="Enter the source code/git repo link to your project. (255 character limit)")
	content = tinymce_models.HTMLField(blank=True, help_text='To use Prism.js for code: <pre><code class="language-css">p { color: red }</code></pre>')
	thumbnail = models.ImageField(upload_to='static/uploads/projects', blank=True, help_text="Your projects featured thumbnail image (Download template here: <a href='" + SITE_URL +"/static/downloads/projectThumbTemplate.psd' downlod='" + SITE_URL + "/static/downloads/projectThumbTemplate.psd'>Thumbnail Template</a>)") # There is an thumbnail upload field. Niiiice.
	enabled = models.BooleanField('enabled')
	featured = models.BooleanField(default=False)

	permalink = models.SlugField(max_length=40, unique=True, blank=True)

	# A routine to show the thumbnail easily (Like in the admin panel)
	def admin_thumbnail(self):
		return format_html('<img src="%s/%s" width="150" height="auto" />' % (SITE_URL, self.thumbnail))

	admin_thumbnail.short_description = 'Project Image' # admin_thumbnail won't work without these
	admin_thumbnail.allow_tags = True # Allow tags to be rendered properly

	# For sorting in admin
	class Meta(object):
		ordering = ['order']

	# To prevent outputting <Question: Question Object> which is not helpful for examination, we can fix that by
	# adding this __str__ method to the class to actually see whats in the object
	#def __str__(self):
	#	return self.title

	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		# Make title URL safe
		return reverse('project_permalink', kwargs={"permalink": self.permalink})

class ProjectImage(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE) # Create relationship with Project. On Project delete, delete line item.
	order = models.PositiveIntegerField(default=0, blank=False, null=False) #adminSortable field
	image = models.ImageField(upload_to='static/uploads/projects', blank=True, max_length=255)
	alt = models.CharField(max_length=60, blank=True, help_text="Image's alt text (60 character limit)")

	# For sorting in admin
	class Meta(object):
		ordering = ['order']

	def __str__(self):
		return self.alt