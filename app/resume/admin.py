from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
from .models import Job
from .models import Institution
from .models import Skillset
from .models import Achievement

class JobAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ['position', 'company', 'start_date', 'end_date', 'current', 'enabled']
class InstitutionAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ['certificate', 'name', 'end_date']
class SkillsetAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ['name', 'skills']
class AchievementAdmin(SortableAdminMixin, admin.ModelAdmin):
	list_display = ['item']

# Register model to be viewed by Django Admin panel
admin.site.register(Job, JobAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Achievement, AchievementAdmin)