from django.db import models
# Create your models here.
class Movie(models.Model):
    Title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(max_length=255,null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    genre = models.CharField(max_length=100,null=True,blank=True)
    length = models.PositiveIntegerField(null=True,blank=True)
    image_card = models.ImageField(upload_to='movie_images/',null=True,blank=True)
    image_cover = models.ImageField(upload_to='movie_images/',null=True,blank=True)
    # video = models.FileField(upload_to='movie_videos/')
    movie_views  = models.IntegerField(default=0,null=True,blank=True)


