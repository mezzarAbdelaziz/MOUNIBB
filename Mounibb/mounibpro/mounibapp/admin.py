from django.contrib import admin
from .models import ResearcherProfile, ResearchProject, Publication

admin.site.register(ResearcherProfile)
admin.site.register(ResearchProject)
admin.site.register(Publication)