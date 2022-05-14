from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render

def index(request):
    #return HttpResponse("<h1>This is Blog Home Page</h1>")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("<h1>This is Blog About Page</h1>")
    return render(request,'blog/about.html')