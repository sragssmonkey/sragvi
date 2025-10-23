from cloudinary.models import CloudinaryField
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    gif = CloudinaryField('gif', blank=True, null=True)

    def __str__(self):
        return self.title
