from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# So this is where you add models so you can use them in Django's admin panel
from .models import Project

# Make customizations like filters and fieldsets to make browsing in the manager easier
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ['title','description','stack','enabled']

# Register project model to be viewed by Django Admin panel
admin.site.register(Project, ProjectAdmin)