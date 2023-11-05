from django import forms

class CrearInsigniaForm(forms.Form):
    title = forms.CharField(label="Nombre de insignia", max_length=200)
    description = forms.CharField(label="Descripcion y requisitos", widget=forms.Textarea)

class CrearProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)