from django.db import models

# Create your models here.
class Project(models.Model):
    """
    class Project to enable uploading of projects and project details by the administrator
    """
    image = models.ImageField(upload_to = 'project_images/')
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=100)
    project_category = models.CharField(max_length=50)