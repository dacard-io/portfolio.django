# Context processor for Resume app that makes data available to all templates without having to include to every page context!
# Include this file in settings.py in TEMPLATE_CONTEXT_PROCESSORS
# 
from .models import Job
from .models import Institution
from .models import Skillset
from .models import Achievement

def resume_processor(request):
	#jobs = Job.objects.all()
	#institutions = Institution.objects.all()
	#skillsets = Skillset.objects.all()
	#achievements = Achievement.objects.all()

	# Return data to template
	return {
		'resume_jobs': Job.objects.all(),
		'resume_institutions': Institution.objects.all(),
		'resume_skillsets': Skillset.objects.all(),
		'resume_achievements': Achievement.objects.all()
	}

# Then simply call into template: {{resume_jobs}}