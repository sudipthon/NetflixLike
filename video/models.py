from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    video_id = models.CharField(max_length=220)
    active = models.BooleanField(default=True)
    # video = models.FileField(upload_to='videos/')
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




# proxy_meaning=a figure that can be used to represent the value of something in a calculation
    
    #passing video as arg and creating meta class with proxy = True will create proxy model which simply creating another database table with same fields as Video model without creating another table fields
class VideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Proxy Video'
        verbose_name_plural = 'Proxy Videos'

   