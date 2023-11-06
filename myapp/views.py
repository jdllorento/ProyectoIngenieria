from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Insignia, UserInsignias
from .forms import CrearInsigniaForm, AsignarInsignia

# Create your views here.

def home(request):
    title = 'Home page of MagnetoInsignias'
    return render(request, 'home.html', {
        'title' : title
    })

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def crear_insignia(request):
    if request.method == 'GET':
        return render(request, 'crear_insignia.html', {
        'form':CrearInsigniaForm()
        })
    else:
        Insignia.objects.create(title = request.POST['nombre'], imagen = request.POST['imagen'], description = "Prueba")
        return redirect('mybadges')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def mybadges(request):
    badges = Insignia.objects.filter(obtenida=True)
    return render(request, 'my_badges.html', {
        'badges': badges
    })

def profile(request):
    return render(request, 'profile.html')

def asignbadge(request):
    if request.method == 'GET':
         return render(request, 'asignar_insignia.html', {
        'form':AsignarInsignia()
        })
    else:
        UserInsignias.objects.create(user_id = request.POST['usuario'], insignia_id = request.POST['insignia'])
        return redirect('home')