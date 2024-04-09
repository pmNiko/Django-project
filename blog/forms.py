from django import forms

class CreateNewtask(forms.Form):
    title = forms.CharField(label='Titulo de la tarea', max_length=200)
    description = forms.CharField(label="Descripción de la tarea", widget=forms.Textarea(attrs={"rows": "5", "required": False}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del Proyecto', max_length=200)
    