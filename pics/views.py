from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my gallery')

def pictures(request):
    return render(request, 'all-pics/pictures.html')