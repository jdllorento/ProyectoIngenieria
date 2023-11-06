from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('perfil/', views.profile, name="perfil"),
    path('crear_insignia/', views.crear_insignia, name="crear_insignia"),
    path('login/', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('mybadges/', views.mybadges, name="mybadges"),
    path('profile/', views.profile, name="perfil"),
    path('asignar/', views.asignbadge, name="asignar")
]