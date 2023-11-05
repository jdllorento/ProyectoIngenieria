from django.contrib import admin
from .models import Project, Insignia, User
# Register your models here.

admin.site.register(Project)
admin.site.register(Insignia)
admin.site.register(User)