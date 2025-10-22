from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    gif = models.ImageField(upload_to='projects_gifs/', blank=True, null=True)  # upload GIFs
    
    def __str__(self):
        return self.title
