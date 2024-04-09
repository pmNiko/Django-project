from django import forms

class CreateNewtask(forms.Form):
    title = forms.CharField(
        label='Titulo de la tarea', 
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    description = forms.CharField(
        label="Descripción de la tarea", 
        widget=forms.Textarea(
            attrs={
                "rows": "5", 
                "required": False, 
                'class': 'input'
            })
    )

class CreateNewProject(forms.Form):
    name = forms.CharField(
        label='Nombre del Proyecto', 
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    