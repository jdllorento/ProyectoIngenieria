# Generated by Django 4.2.4 on 2023-11-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_insignia_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='insignias',
            field=models.ManyToManyField(to='myapp.insignia'),
        ),
    ]
