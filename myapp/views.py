from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, Insignia

# Create your views here.

def home(request):
    title = 'Home page of MagnetoInsignias'
    return render(request, 'home.html', {
        'title' : title
    })

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def insignias(request):
    #insignias = Insignia.objects.get(title=title)
    return render(request, 'insignias.html')