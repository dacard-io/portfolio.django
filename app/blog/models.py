from django.db import models
from django.utils import timezone # To calculate by timezone
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
	post_title = models.CharField(max_length=60,help_text="60 character limit")
	post_description = models.CharField(max_length=150,help_text="150 character limit")
	post_content = tinymce_models.HTMLField(blank=True)
	pub_date = models.DateTimeField('date published')
	enabled = models.BooleanField('enabled')

	# Add a method for showing whether a question was published recently
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	# To prevent outputting <Question: Question Object> which is not helpful for examination, we can fix that by
	# adding this __str__ method to the class to actually see whats in the object
	def __str__(self):
		return self.post_title