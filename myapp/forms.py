from django import forms

class CrearInsigniaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de insignia", max_length=200)
    descripcion = forms.CharField(label="Descripción de la insignia", max_length=300)
    imagen = forms.ImageField(required=True)

class AsignarInsignia(forms.Form):
    usuario = forms.IntegerField(label="Id del usuario a asignar")
    insignia = forms.IntegerField(label="Id insignia a asignar")