from django.contrib import admin
from .models import VideoAllProxy,VideoPublishedProxy
# Register your models here.


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['__str__','video_id']
    search_fields = ['title','description']
    class Meta:
        model = VideoAllProxy        

admin.site.register(VideoAllProxy,VideoAllAdmin)

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['__str__','video_id']
    search_fields = ['title','description']
    class Meta:
        model = VideoPublishedProxy
    
    def get_queryset(self,request):
        return VideoProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy,VideoPublishedProxyAdmin)