from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location>\d+)', views.a_location,name='search_location'),
    url(r'^category/(?P<category>\d+)', views.a_category,name='search_category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)