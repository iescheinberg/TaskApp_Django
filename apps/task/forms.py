from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'completado']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        