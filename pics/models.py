from django.db import models
import datetime as dt 

# Create your models here.

class Location(models.Model):
    image_location = models.CharField(max_length=60)
    
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations
    
    def __str__(self):
        return self.image_location
    
class Category(models.Model):
    image_category = models.CharField(max_length=60)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.save()
        
    def update_category(self):
        self.update_category()
        
    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
    
    @classmethod
    def get_all_categories(cls):
        all_categories = Category.objects.all()
        return all_categories

    def __str__(self):
        return self.image_category
    
class Image(models.Model):
    '''
    Class for functions that affect the image 
    '''
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length = 40)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length = 60,blank =True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update_image()
        
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
        
    @classmethod
    def get_image_by_id(cls,id):
        single_image = Image.objects.get(id=id)
        return image
    
    @classmethod
    def search_image(cls,search_category):
        image_category = Image.objects.filter(search_category=search_category)
        return images_category
    
    @classmethod
    def filter_by_location(cls,filter_location):
        image_location = Image.object.filter(location_id=location_id)
        return location_id
        
    def __str__(self):
        return self.name
    
