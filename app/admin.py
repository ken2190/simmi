from django.contrib import admin
from .models import ImageModel
from django.utils.html import format_html

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.images.url))

    thumbnail.short_description = "photo"

    list_display = ('id','thumbnail' ,'heading',)
    list_display_links = ('id','thumbnail','heading')
    search_fields = ('heading',)
    # list_filter = ('heading',)

admin.site.register(ImageModel, ImageAdmin)