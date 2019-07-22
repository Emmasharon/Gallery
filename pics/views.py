from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category
import datetime as dt

# Create your views here.
def index(request):
    images = Image.get_all_images()
    locations = Location.get_locations()
    categories = Category.get_all_categories()
    return render(request,'index.html',{'images':images, 'categories':categories, 'locations':locations})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images_found = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'images':images_found, 'locations':locations})
    else:
        message = "Search here"
        return render(request, 'search.html',{'message':message})

