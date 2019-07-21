from django.contrib import admin
from .models import Category, Image ,Location

class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal = ('Category',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)
