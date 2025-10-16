from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField('image', blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    art_id = models.AutoField(primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image_url = CloudinaryField('image')
    image_width = models.PositiveIntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    alt_text = models.CharField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title