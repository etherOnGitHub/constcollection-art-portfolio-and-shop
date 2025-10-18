from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    cover_image = CloudinaryField('image')
    video = CloudinaryField('video', resource_type='video', blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title