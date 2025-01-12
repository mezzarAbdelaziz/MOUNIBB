from django.db import models
from django.contrib.auth.models import User

# Profile Model to store additional information for users
class ResearcherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.user.username

# Model for Research Projects
class ResearchProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    researchers = models.ManyToManyField(ResearcherProfile, related_name="projects")
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Ongoing')

    def __str__(self):
        return self.title

# Model for Research Publications
class Publication(models.Model):
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(ResearcherProfile, related_name="publications")
    journal_name = models.CharField(max_length=255)
    year_published = models.IntegerField()

    def __str__(self):
        return self.title


