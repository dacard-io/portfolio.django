from django.db import models
from django.utils import timezone # To calculate by timezone
from tinymce import models as tinymce_models

# Create your models here.
class Job(models.Model):
	order = models.PositiveIntegerField(default=0, blank=False, null=False) #adminSortable field

	company = models.CharField(max_length=150,help_text="150 character limit")
	position = models.CharField(max_length=60,help_text="60 character limit")
	description = models.TextField(help_text="Describe your job position")

	start_date = models.DateField('When you started working')
	end_date = models.DateField('When you stopped working', blank=True, null=True) # blank and null to set the field to be unrequired
	current = models.BooleanField('Current Position', help_text="Are you currently working at this position?") # A bool to hold whether this
	enabled = models.BooleanField('Enable Position', default=True, help_text="Do you want to show this on resume?")

	# For sorting in admin
	class Meta(object):
		ordering = ['order']

# Hold educational insitutions
class Institution(models.Model):
	order = models.PositiveIntegerField(default=0, blank=False, null=False) #adminSortable field

	certificate = models.CharField(max_length=150,help_text="Degree/Diploma name")
	name = models.CharField(max_length=150,help_text="Name of institution")
	end_date = models.DateField('Completion Date')

	# For sorting in admin
	class Meta(object):
		ordering = ['order']

class Skillset(models.Model):
	order = models.PositiveIntegerField(default=0, blank=False, null=False) #adminSortable field

	name = models.CharField(max_length=150,help_text="Name of skillset (i.e, Front-end/Services)")
	skills = models.TextField(help_text="List your skills, seperate with commas. Just a regular text area.")
	# One to Many relationship to skills for linking? Not for now I guess
	
	# For sorting in admin
	class Meta(object):
		ordering = ['order']

class Achievement(models.Model):
	order = models.PositiveIntegerField(default=0, blank=False, null=False) #adminSortable field
	
	item = models.TextField(help_text="Information about the achievement")

	# For sorting in admin
	class Meta(object):
		ordering = ['order']