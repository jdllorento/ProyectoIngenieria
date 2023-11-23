from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Insignia
from .forms import CrearInsigniaForm, AsignarInsignia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def user_is_admin(request):
    return request.groups.filter(name='Admins').exists()

def home(request):
    title = 'Home page of MagnetoInsignias'
    return render(request, 'home.html', {
        'title' : title
    })

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

@user_passes_test(user_is_admin)
def crear_insignia(request):
        if request.method == 'POST':
            form = CrearInsigniaForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['nombre']
                description = form.cleaned_data['descripcion']
                imagen = form.cleaned_data['imagen']
                
                insignia = Insignia(
                    title=title,
                    description=description,
                    imagen=imagen,
                )

                insignia.save()
                return redirect('mybadges')
        else:
            form = CrearInsigniaForm()

        return render(request, 'crear_insignia.html', {'form':form})



#    try:
#        if request.method == 'GET':
#            return render(request, 'crear_insignia.html', {
#                'form':CrearInsigniaForm()
#            })
#        else:
#            form = CrearInsigniaForm(request.POST, request.FILES)
#            form.save()
#            Insignia.objects.create(title = request.POST['nombre'], imagen = request.POST['imagen'], description = "Prueba")
#            return redirect('mybadges')
#    except:
#        return HttpResponse('No eres admin')

def login(request):
    return render(request, 'login.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('User created succesfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('passwords do not match')

def mybadges(request):
    badges = Insignia.objects.filter(portador=request.user)
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
        #Insignia.portador.add(user_id = request.POST['usuario'], insignia_id = request.POST['insignia'])
        ins = Insignia.objects.get(id = request.POST['insignia'])
        us = User.objects.get(id = request.POST['usuario'])
        a = ins.portador.add(us)
        ins.save()
        return redirect('home')