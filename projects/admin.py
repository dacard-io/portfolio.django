from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# So this is where you add models so you can use them in Django's admin panel
from .models import Project
from .models import ProjectImage

class ProjectImageInline(admin.TabularInline):
	model = ProjectImage
	extra = 0

# Make customizations like filters and fieldsets to make browsing in the manager easier
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ['admin_thumbnail','title','description','stack','enabled']
	# Inline models for admin
	inlines = [ProjectImageInline]

# Register project model to be viewed by Django Admin panel
admin.site.register(Project, ProjectAdmin)