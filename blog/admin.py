from django.contrib import admin

# So this is where you add models so you can use them in Django's admin panel
from .models import Post

# Make customizations like filters and fieldsets to make browsing in the manager easier
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'permalink', 'description', 'pub_date', 'published']

# Register choice model to be viewed by Django Admin panel
admin.site.register(Post, PostAdmin)


# Lets customize and reorder the fields for questions
# Simple way of doing it, but its best to use the next example for the fields
#class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question_text'] # Will put the date feild first

# Create a class to add inline options to inside th Question admin form. Choose the Choice model, and automatically ask for 3 options
# You can use either admin.StackedInline, but tabular makes it more table like and saves space
'''
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

# Its better to use fieldsets to customize the form
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				{'fields': ['question_text']}), # The first parameter groups said field under a heading
		('Date information',{'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently') # Add columns to the list view of the Question model
	list_filter = ['pub_date'] # Add the ability to sort by pub_date, adds a little window on the right of the table
	search_fields = ['question_text'] # Add the ability to search by question_text field

admin.site.register(Question, QuestionAdmin) # Registers a default form representation of the question model
'''