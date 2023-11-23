# Generated by Django 4.2.7 on 2023-11-22 20:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0012_alter_insignia_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='insignias',
        ),
        migrations.AddField(
            model_name='insignia',
            name='portador',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]