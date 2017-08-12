from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from tinymce import models as tinymce_models
from django.conf.urls.static import static # To get static directories to show thumbnail

PROJECT_ROOT = '//localhost:8000/'

# Create your models here.
class Project(models.Model):

	title = models.CharField(max_length=60,help_text="60 character limit")

	tag_choices = (
		('uncategorized', 'Uncategorized'),
		('web-app', 'Web Apps'),
		('android-app', 'Android Apps'),
		('website', 'Websites'),
		('ecommerce', 'e-Commerce'),
		('plugins-extensions', 'Plugins & Extensions'),
	) # Remember, the first parameter is set in the DB. The second is the one to appear in labels
	tag = models.CharField(max_length=60, choices=tag_choices, default="uncategorized", help_text="Tag your project for categorization.")
	
	description = models.TextField(max_length=256, help_text="Describe your project. (256 character limit)")
	stack = models.CharField(max_length=256, blank=True, help_text="Describe your project's used tech stack. (256 character limit)")
	link = models.CharField(max_length=256, help_text="Enter the link to your project. (256 character limit)")
	image = models.ImageField(upload_to='static/uploads/projects') # There is an image upload field. Niiiice.
	enabled = models.BooleanField('enabled')

	# A routine to show the image easily (Like in the admin panel)
	def admin_thumbnail(self):
		return format_html('<img src="%s%s" width="150" height="auto" />' % (PROJECT_ROOT, self.image))

	admin_thumbnail.short_description = 'Project Image' # admin_thumbnail won't work without these
	admin_thumbnail.allow_tags = True # Allow tags to be rendered properly

	# To prevent outputting <Question: Question Object> which is not helpful for examination, we can fix that by
	# adding this __str__ method to the class to actually see whats in the object
	def __str__(self):
		return self.title