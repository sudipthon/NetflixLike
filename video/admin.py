from django.contrib import admin
from .models import Video,VideoProxy
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ['__str__','video_id']
    search_fields = ['title','description']
    list_filter = ['active','created']
    class Meta:
        model = Video
        

admin.site.register(Video)
admin.site.register(VideoProxy)