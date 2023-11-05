from django import forms

class CrearInsigniaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de insignia", max_length=200)
    imagen = forms.ImageField(required=False)

class CrearProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)