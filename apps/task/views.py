from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.

# Lista de tareas
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})


# Borrar tarea
def agregar_tarea(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        
    return render(request, 'task/agregar_tarea.html', {'form': form})



# Borrar tarea
def borrar_tarea(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

