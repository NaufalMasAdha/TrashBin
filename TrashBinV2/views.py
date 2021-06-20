from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse('About US')
    return render(request, 'about.html')

def homepage(request):
    #return HttpResponse('Home Page')
    return render(request, 'homepage.html')

def map(request):
    return render(request, 'map.html')
