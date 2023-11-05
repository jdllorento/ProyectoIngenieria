from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project, Insignia
from .forms import CrearInsigniaForm, CrearProject

# Create your views here.

def home(request):
    title = 'Home page of MagnetoInsignias'
    return render(request, 'home.html', {
        'title' : title
    })

def about(request):
    return render(request, 'about.html')

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects' : projects
    })

def insignias(request):
    #insignias = Insignia.objects.get(title=title)
    insignias = Insignia.objects.all()
    return render(request, 'insignias.html', {
        'insignias' : insignias
    })

def profile(request):
    return render(request, 'profile.html')

def crear_insignia(request):
    if request.method == 'GET':
        return render(request, 'crear_insignia.html', {
        'form':CrearInsigniaForm()
        })
    else:
        Insignia.objects.create(title = request.POST['title'], description = request.POST['description'], project_id=2)
        return redirect('insignias')


def crear_project(request):
    if request.method == 'GET':
        return render(request, 'crear_project.html', {
        'form': CrearProject()
        })
    else:
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        return render(request, 'crear_project.html', {
        'form': CrearProject()
        })
    