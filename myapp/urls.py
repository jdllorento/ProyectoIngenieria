from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('insignias/', views.insignias, name="insignias"),
    path('perfil/', views.profile, name="perfil"),
    path('crear_insignia/', views.crear_insignia, name="crear_insignia"),
    path('crear_project/', views.crear_project, name="crear_proyecto"),
    path('login/', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('mybadges/', views.mybadges, name="mybadges"),
    path('profile/', views.profile, name="perfil"),
]